
from openai import OpenAI
import os
import json

# Initialize OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set. Please add it in the Secrets tool.")
client = OpenAI(api_key=api_key)

def generate_quiz(prompt, num_questions=5):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful quiz maker. Generate quiz questions in JSON format with 'question' and 'options' fields. Each question should have 4 multiple choice options labeled A, B, C, D."},
                {"role": "user", "content": f"Generate {num_questions} multiple-choice questions about: {prompt}. Return as a JSON array where each question has 'question' and 'options' fields."}
            ],
            temperature=0.7,
        )
        
        # Parse the response to extract quiz data
        quiz_text = response.choices[0].message.content
        
        # Try to parse JSON response
        try:
            quiz_data = json.loads(quiz_text)
            return quiz_data
        except json.JSONDecodeError:
            # If not valid JSON, create structured format from text
            questions = []
            lines = quiz_text.strip().split('\n')
            current_question = None
            current_options = []
            
            for line in lines:
                line = line.strip()
                if line and (line.startswith(f"{len(questions)+1}.") or line.startswith("Q")):
                    if current_question:
                        questions.append({"question": current_question, "options": current_options})
                    current_question = line
                    current_options = []
                elif line and (line.startswith("A)") or line.startswith("B)") or line.startswith("C)") or line.startswith("D)")):
                    current_options.append(line)
            
            if current_question:
                questions.append({"question": current_question, "options": current_options})
            
            return questions
            
    except Exception as e:
        print(f"Error generating quiz: {e}")
        # Return fallback quiz
        return [{"question": f"Error generating quiz: {str(e)}", "options": ["Please check your API key", "Try again", "Check console for details", "Contact support"]}]
