from flask import Flask, request, jsonify, send_from_directory, session, redirect, url_for
from flask_cors import CORS
import os
import sys
from dotenv import load_dotenv
import secrets

# Load environment variables
load_dotenv()

sys.path.append('backend')
from quiz_generator import generate_quiz
from auth import init_db, register_user, login_user, save_result, get_leaderboard, get_user_results

app = Flask(__name__, static_folder='frontend', static_url_path='')
app.secret_key = secrets.token_hex(16)  # Generate a random secret key
CORS(app, supports_credentials=True)  # Allows requests from frontend with credentials

# Initialize database
init_db()

# Route to serve the HTML page
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# Authentication routes
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400
    
    if register_user(username, password):
        return jsonify({"message": "Registration successful"}), 201
    else:
        return jsonify({"error": "Username already exists"}), 409

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    user_id = login_user(username, password)
    if user_id:
        session['user_id'] = user_id
        session['username'] = username
        return jsonify({"message": "Login successful", "user_id": user_id, "username": username}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({"message": "Logout successful"}), 200

@app.route('/check_auth', methods=['GET'])
def check_auth():
    if 'user_id' in session:
        return jsonify({
            "authenticated": True, 
            "user_id": session['user_id'], 
            "username": session['username']
        }), 200
    else:
        return jsonify({"authenticated": False}), 401

# API route to generate quiz
@app.route('/generate_quiz', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "General Knowledge")
    num_questions = int(data.get("num_questions", 5))

    # Generate real quiz using OpenAI
    quiz = generate_quiz(prompt, num_questions)
    return jsonify({"quiz": quiz})

# API route to save quiz results
@app.route('/save_result', methods=['POST'])
def save_quiz_result():
    if 'user_id' not in session:
        return jsonify({"error": "Not authenticated"}), 401
    
    data = request.get_json()
    score = data.get("score")
    total_questions = data.get("total_questions")
    topic = data.get("topic", "General")
    
    if score is None or total_questions is None:
        return jsonify({"error": "Score and total questions are required"}), 400
    
    save_result(session['user_id'], score, total_questions, topic)
    return jsonify({"message": "Result saved successfully"}), 200

# API route to get leaderboard
@app.route('/leaderboard', methods=['GET'])
def get_quiz_leaderboard():
    leaderboard = get_leaderboard()
    return jsonify({"leaderboard": leaderboard}), 200

# API route to get user results
@app.route('/user_results', methods=['GET'])
def get_user_quiz_results():
    if 'user_id' not in session:
        return jsonify({"error": "Not authenticated"}), 401
    
    results = get_user_results(session['user_id'])
    return jsonify({"results": results}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
