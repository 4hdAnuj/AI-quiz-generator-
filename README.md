# 🤖 AI Quiz Generator

A modern web application that generates AI-powered quizzes using Google's Gemini AI. Features user authentication, live leaderboards, and result tracking.

## ✨ Features

- **AI-Powered Quiz Generation**: Create quizzes on any topic using Google Gemini AI
- **User Authentication**: Secure registration and login system
- **Live Leaderboard**: Real-time rankings with medal system
- **Result Tracking**: Personal quiz history and performance analytics
- **Modern UI**: Beautiful, responsive design with tabbed interface
- **Database Storage**: SQLite database for persistent data storage

## 🚀 Quick Start

### Option 1: One-Click Setup (Recommended)
1. Double-click `setup.bat` to install dependencies and start the application
2. Open your browser and go to `http://localhost:3000`

### Option 2: Manual Setup
1. Install Python 3.8+ if not already installed
2. Run: `py -m pip install -r backend/requirements.txt`
3. Set environment variable: `set GEMINI_API_KEY=AIzaSyCnn4Art8B1Uog0zRcOethbzkkJo4tyzAg`
4. Run: `py main.py`
5. Open browser to `http://localhost:3000`

### Option 3: Quick Run (if dependencies already installed)
1. Double-click `run.bat` to start the application
2. Open your browser and go to `http://localhost:3000`

## 📁 Project Structure

```
ai-quiz-generator/
├── main.py                 # Main Flask application
├── backend/
│   ├── auth.py            # Authentication and database functions
│   ├── quiz_generator.py  # AI quiz generation logic
│   └── requirements.txt   # Python dependencies
├── frontend/
│   └── index.html         # Web interface
├── setup.bat              # Complete setup script
├── run.bat                # Quick run script
└── README.md              # This file
```

## 🎯 How to Use

### 1. Registration & Login
- Click "Login/Register" tab
- Create a new account or login with existing credentials
- Your session will be maintained until you logout

### 2. Taking Quizzes
- Navigate to "Take Quiz" tab
- Enter any topic (e.g., "Science", "History", "Programming")
- Choose number of questions (1-20)
- Click "Generate Quiz" to create AI-powered questions
- Select your answers and submit

### 3. Viewing Results
- **Leaderboard**: See top performers across all users
- **My Results**: View your personal quiz history and performance

## 🔧 Technical Details

### Backend Technologies
- **Flask**: Web framework
- **SQLite**: Database for user data and results
- **Google Gemini AI**: Quiz generation
- **Werkzeug**: Password hashing and security

### Frontend Technologies
- **HTML5/CSS3**: Modern, responsive design
- **JavaScript**: Interactive functionality
- **Fetch API**: Backend communication

### API Endpoints
- `POST /register` - User registration
- `POST /login` - User authentication
- `POST /logout` - Session termination
- `GET /check_auth` - Authentication verification
- `POST /generate_quiz` - Generate AI quiz
- `POST /save_result` - Save quiz results
- `GET /leaderboard` - Get leaderboard data
- `GET /user_results` - Get user's quiz history

## 🛠️ Configuration

### Environment Variables
- `GEMINI_API_KEY`: Your Google Gemini API key (already configured)

### Database
- SQLite database automatically created at `backend/database.db`
- Tables: `users`, `results`

## 🔒 Security Features

- Password hashing using Werkzeug
- Session-based authentication
- SQL injection prevention
- Input validation and sanitization

## 🎨 UI Features

- **Tabbed Interface**: Easy navigation between features
- **Responsive Design**: Works on desktop and mobile
- **Interactive Elements**: Hover effects and animations
- **Real-time Updates**: Live leaderboard and results
- **Alert System**: Success/error notifications

## 📊 Database Schema

### Users Table
- `id`: Primary key
- `username`: Unique username
- `password`: Hashed password
- `created_at`: Account creation timestamp

### Results Table
- `id`: Primary key
- `user_id`: Foreign key to users
- `score`: Quiz score
- `total_questions`: Total questions in quiz
- `topic`: Quiz topic
- `percentage`: Calculated percentage
- `created_at`: Quiz completion timestamp

## 🚀 Deployment

### Local Development
- Use `py main.py` to run in development mode
- Application runs on `http://localhost:3000`

### Production Deployment
- Use a production WSGI server (Gunicorn, uWSGI)
- Set up proper environment variables
- Configure reverse proxy (Nginx, Apache)
- Use HTTPS for security

## 🐛 Troubleshooting

### Common Issues

1. **"Module not found" errors**
   - Run: `py -m pip install -r backend/requirements.txt`

2. **"API key not configured"**
   - Ensure `GEMINI_API_KEY` environment variable is set
   - Check `.env` file exists and contains the key

3. **Port already in use**
   - Kill existing process: `taskkill /F /IM python.exe`
   - Or change port in `main.py`

4. **Database errors**
   - Delete `backend/database.db` to reset
   - Restart application

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

---

**Happy Quizzing! 🎉** 