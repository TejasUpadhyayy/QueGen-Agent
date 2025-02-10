# AI Question Generator  

An intelligent AI agent that autonomously generates quiz questions from any topic or text using Google’s Gemini API. Designed for educators, students, and content creators, it adapts to different difficulty levels and question formats to enhance the learning experience.  

## Capabilities  
- Supports multiple question types: **Multiple Choice, True/False, Fill-in-the-Blank, Short Answer**  
- Adjustable **difficulty levels**  
- Customizable **number of questions**  
- Expands context for brief topics to generate meaningful questions  
- Web interface built with **Streamlit** for ease of use  

## Setup  
1. Clone the repository  
2. Install dependencies: `pip install -r requirements.txt`  
3. Create a `.env` file and add your API key: `GEMINI_API_KEY=your_api_key`  
4. Run the application: `streamlit run app.py`  

## Usage Example  
```python
# Input text
text = "Python is a high-level programming language..."

# Configure options
num_questions = 5
difficulty = "Medium"
question_type = "Multiple Choice"

# Generate questions
generator = QuestionGenerator()
questions = generator.generate_questions(text, num_questions, difficulty, question_type)
```  

## Requirements  
See `requirements.txt` for a full list of dependencies.
