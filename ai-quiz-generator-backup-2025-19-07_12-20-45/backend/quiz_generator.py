
import google.generativeai as genai
import os
import json

# Initialize Gemini client
def get_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("WARNING: GEMINI_API_KEY environment variable is not set. Please add it in the Secrets tool.")
        return None
    try:
        genai.configure(api_key=api_key)
        # Use gemini-1.5-flash for faster responses
        model = genai.GenerativeModel(
            'gemini-1.5-flash',
            system_instruction="You are a quick quiz generator. Always respond with valid JSON format."
        )
        return model
    except Exception as e:
        print(f"Error initializing Gemini client: {e}")
        return None

def generate_quiz(prompt, num_questions=5):
    model = get_gemini_client()
    if not model:
        return [{"question": "Gemini API key not configured. Please add GEMINI_API_KEY in the Secrets tool.", "options": ["A) Go to Tools > Secrets", "B) Add GEMINI_API_KEY", "C) Set your API key value", "D) Restart the application"]}]
    
    try:
        # Create a concise prompt for faster response
        system_prompt = f"""Create {num_questions} multiple-choice questions about {prompt}. Return only valid JSON:

[{{"question": "Question text?", "options": ["A) option1", "B) option2", "C) option3", "D) option4"]}}]

Topic: {prompt}
Questions: {num_questions}"""
        
        # Configure generation parameters for faster response
        generation_config = {
            "temperature": 0.7,
            "top_p": 0.8,
            "top_k": 40,
            "max_output_tokens": 2048,
        }
        
        response = model.generate_content(system_prompt, generation_config=generation_config)
        quiz_text = response.text
        
        # Try to parse JSON response
        try:
            # Clean the response text (remove any markdown formatting)
            clean_text = quiz_text.strip()
            if clean_text.startswith('```json'):
                clean_text = clean_text[7:]
            if clean_text.endswith('```'):
                clean_text = clean_text[:-3]
            clean_text = clean_text.strip()
            
            quiz_data = json.loads(clean_text)
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
            
            return questions if questions else [{"question": "Generated quiz parsing failed", "options": ["A) Try again", "B) Check API key", "C) Simplify topic", "D) Contact support"]}]
            
    except Exception as e:
        print(f"Error generating quiz: {e}")
        # Return fallback quiz
        return [{"question": f"Error generating quiz: {str(e)}", "options": ["A) Please check your API key", "B) Try again", "C) Check console for details", "D) Contact support"]}]
