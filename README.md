# AI Question Generator

An AI-powered educational tool that automatically generates quiz questions from any topic or text using Google's Gemini API.

## Features
- Multiple question types (MCQ, True/False, Fill-in-blank, Short Answer)
- Adjustable difficulty levels
- Custom number of questions
- Context expansion for brief topics
- Web interface built with Streamlit

## Setup
1. Clone repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create `.env` file with `GEMINI_API_KEY=your_api_key`
4. Run: `streamlit run app.py`

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
See requirements.txt for full list.