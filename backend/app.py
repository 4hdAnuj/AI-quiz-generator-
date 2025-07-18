from flask import Flask, request, jsonify
from quiz_generator import generate_quiz
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows requests from frontend

# Homepage route to avoid "Not Found" error
@app.route('/')
def home():
    return "✅ Flask backend is running! Use POST /generate_quiz to get a quiz."

# POST route to generate quiz
@app.route('/generate_quiz', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")
    num_questions = int(data.get("num_questions", 5))
    quiz = generate_quiz(prompt, num_questions)
    return jsonify({"quiz": quiz})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
