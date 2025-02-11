import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from typing import Optional, Dict, List

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise EnvironmentError("GEMINI_API_KEY not found in environment variables")

genai.configure(api_key=API_KEY)

class QuestionGenerator:
    QUESTION_FORMATS: Dict[str, str] = {
        "Multiple Choice": """
            - MCQ: {question}
              A) {option1}
              B) {option2}
              C) {option3}
              D) {option4}
              Answer: {answer}
        """,
        "True/False": """
            - True/False: {question}
              Answer: {answer}
        """,
        "Fill-in-the-Blank": """
            - Fill-in-the-blank: {question}
              Answer: {answer}
        """,
        "Short Answer": """
            - Short Answer: {question}
              Answer: {answer}
        """
    }

    def __init__(self, model_name: str = "gemini-pro"):
        self.model = genai.GenerativeModel(model_name)

    def fetch_context(self, topic: str) -> str:
        """Fetch additional context for short inputs."""
        try:
            prompt = f"Provide a brief, informative paragraph about {topic}."
            response = self.model.generate_content(prompt)
            return response.text if response.text else f"{topic} is a broad topic. Please specify further."
        except Exception as e:
            st.error(f"Error fetching context: {str(e)}")
            return topic

    def generate_prompt(self, text: str, num_questions: int, difficulty: str, question_type: str) -> str:
        """Generate formatted prompt for question generation."""
        return f"""Generate {num_questions} {question_type} questions at {difficulty} difficulty from this text:

        {text}

        Format each question as:
        {self.QUESTION_FORMATS[question_type].strip()}
        """

    def generate_questions(self, text: str, num_questions: int, difficulty: str, question_type: str) -> str:
        """Generate questions based on input parameters."""
        if len(text.split()) < 5:
            text = self.fetch_context(text)

        prompt = self.generate_prompt(text, num_questions, difficulty, question_type)
        
        try:
            response = self.model.generate_content(prompt)
            return response.text if response.text else "No questions generated. Please try again."
        except Exception as e:
            st.error(f"Error generating questions: {str(e)}")
            return "Failed to generate questions. Please try again."

def create_ui():
    """Create Streamlit UI components."""
    st.set_page_config(page_title="QueGen Agent", page_icon="📚")
    
    st.title(" QueGen Agent")
    st.write("Enter a topic or text, and the agent will generate quiz questions.")

    # Input components
    user_input = st.text_area("Enter text or topic:", height=150)
    col1, col2 = st.columns(2)
    
    with col1:
        num_questions = st.number_input(
            "Number of questions:",
            min_value=1,
            max_value=20,
            value=5
        )
        difficulty = st.selectbox(
            "Difficulty level:",
            ["Easy", "Medium", "Hard"]
        )
    
    with col2:
        question_type = st.selectbox(
            "Question type:",
            list(QuestionGenerator.QUESTION_FORMATS.keys())
        )

    return user_input, num_questions, difficulty, question_type

def main():
    user_input, num_questions, difficulty, question_type = create_ui()
    generator = QuestionGenerator()

    if st.button("Generate Questions") and user_input:
        with st.spinner("Generating questions..."):
            questions = generator.generate_questions(
                user_input,
                num_questions,
                difficulty,
                question_type
            )
            st.subheader("Generated Questions:")
            st.text_area("", questions, height=300)

if __name__ == "__main__":
    main()
