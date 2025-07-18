from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='frontend', static_url_path='')
CORS(app)  # Allows requests from frontend

# Route to serve the HTML page
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# API route to generate quiz
@app.route('/generate_quiz', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "General Knowledge")
    num_questions = int(data.get("num_questions", 5))

    # Dummy quiz generation logic (replace with real one if needed)
    quiz = []
    for i in range(num_questions):
        quiz.append({
            "question": f"{i+1}. What is something about {prompt}?",
            "options": ["Option A", "Option B", "Option C", "Option D"]
        })

    return jsonify({"quiz": quiz})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
