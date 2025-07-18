
import openai
import os

# Make sure your OpenAI API key is set in Replit secrets or here directly
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_quiz(prompt, num_questions=5):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Or gpt-4 if available to you
        messages=[
            {"role": "system", "content": "You are a helpful quiz maker."},
            {"role": "user", "content": f"Generate {num_questions} multiple-choice questions on: {prompt}"}
        ],
        temperature=0.7,
    )
    return response.choices[0].message["content"]
