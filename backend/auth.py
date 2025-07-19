import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def init_db():
    conn = sqlite3.connect("backend/database.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        score INTEGER,
        total_questions INTEGER,
        topic TEXT,
        percentage REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )''')
    conn.commit()
    conn.close()

def register_user(username, password):
    conn = sqlite3.connect("backend/database.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                  (username, generate_password_hash(password)))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def login_user(username, password):
    conn = sqlite3.connect("backend/database.db")
    c = conn.cursor()
    c.execute("SELECT id, password FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    conn.close()
    if user and check_password_hash(user[1], password):
        return user[0]  # return user_id
    return None

def save_result(user_id, score, total_questions, topic):
    conn = sqlite3.connect("backend/database.db")
    c = conn.cursor()
    percentage = (score / total_questions) * 100
    c.execute("INSERT INTO results (user_id, score, total_questions, topic, percentage) VALUES (?, ?, ?, ?, ?)",
              (user_id, score, total_questions, topic, percentage))
    conn.commit()
    conn.close()

def get_leaderboard():
    conn = sqlite3.connect("backend/database.db")
    c = conn.cursor()
    c.execute("""
        SELECT u.username, r.score, r.total_questions, r.percentage, r.topic, r.created_at
        FROM results r
        JOIN users u ON r.user_id = u.id
        ORDER BY r.percentage DESC, r.created_at DESC
        LIMIT 20
    """)
    results = c.fetchall()
    conn.close()
    
    leaderboard = []
    for row in results:
        leaderboard.append({
            "username": row[0],
            "score": row[1],
            "total_questions": row[2],
            "percentage": round(row[3], 1),
            "topic": row[4],
            "created_at": row[5]
        })
    return leaderboard

def get_user_results(user_id):
    conn = sqlite3.connect("backend/database.db")
    c = conn.cursor()
    c.execute("""
        SELECT score, total_questions, topic, percentage, created_at
        FROM results
        WHERE user_id = ?
        ORDER BY created_at DESC
        LIMIT 50
    """, (user_id,))
    results = c.fetchall()
    conn.close()
    
    user_results = []
    for row in results:
        user_results.append({
            "score": row[0],
            "total_questions": row[1],
            "topic": row[2],
            "percentage": round(row[3], 1),
            "created_at": row[4]
        })
    return user_results
