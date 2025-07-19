# 🚀 Deployment Guide - AI Quiz Generator

## Quick Deploy Options

### Option 1: Render (Recommended - Free & Easy)

1. **Go to [Render.com](https://render.com)** and sign up
2. **Click "New +"** → **"Web Service"**
3. **Connect your GitHub repository**: `https://github.com/4hdAnuj/AI-quiz-generator-`
4. **Configure the service**:
   - **Name**: `ai-quiz-generator`
   - **Environment**: `Python`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python main.py`
5. **Add Environment Variables**:
   - `GEMINI_API_KEY`: `AIzaSyCnn4Art8B1Uog0zRcOethbzkkJo4tyzAg`
6. **Click "Create Web Service"**
7. **Wait for deployment** (2-3 minutes)
8. **Your app will be live at**: `https://your-app-name.onrender.com`

### Option 2: Railway (Free & Fast)

1. **Go to [Railway.app](https://railway.app)** and sign up
2. **Click "New Project"** → **"Deploy from GitHub repo"**
3. **Select your repository**: `4hdAnuj/AI-quiz-generator-`
4. **Add Environment Variable**:
   - `GEMINI_API_KEY`: `AIzaSyCnn4Art8B1Uog0zRcOethbzkkJo4tyzAg`
5. **Deploy automatically**
6. **Your app will be live at**: `https://your-app-name.railway.app`

### Option 3: Heroku (Free Tier Discontinued)

1. **Install Heroku CLI**
2. **Login**: `heroku login`
3. **Create app**: `heroku create your-app-name`
4. **Set environment variable**: `heroku config:set GEMINI_API_KEY=AIzaSyCnn4Art8B1Uog0zRcOethbzkkJo4tyzAg`
5. **Deploy**: `git push heroku main`
6. **Open**: `heroku open`

### Option 4: PythonAnywhere (Free)

1. **Go to [PythonAnywhere.com](https://www.pythonanywhere.com)** and sign up
2. **Go to "Web" tab** → **"Add a new web app"**
3. **Choose "Flask"** and **Python 3.11**
4. **Upload your files** via Files tab
5. **Set up virtual environment**:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.11 ai-quiz-env
   pip install -r requirements.txt
   ```
6. **Configure WSGI file** to point to your app
7. **Add environment variable** in Web app settings
8. **Reload** your web app

### Option 5: Vercel (Free)

1. **Go to [Vercel.com](https://vercel.com)** and sign up
2. **Import your GitHub repository**
3. **Configure build settings**:
   - **Framework Preset**: Other
   - **Build Command**: `pip install -r requirements.txt`
   - **Output Directory**: `.`
   - **Install Command**: `pip install -r requirements.txt`
4. **Add Environment Variable**:
   - `GEMINI_API_KEY`: `AIzaSyCnn4Art8B1Uog0zRcOethbzkkJo4tyzAg`
5. **Deploy**

## 🛠️ Manual Deployment Steps

### Prerequisites
- Python 3.8+
- Git
- Your GitHub repository

### Steps
1. **Clone your repository**:
   ```bash
   git clone https://github.com/4hdAnuj/AI-quiz-generator-.git
   cd AI-quiz-generator-
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variable**:
   ```bash
   export GEMINI_API_KEY=AIzaSyCnn4Art8B1Uog0zRcOethbzkkJo4tyzAg
   ```

4. **Run the application**:
   ```bash
   python main.py
   ```

## 🔧 Production Configuration

### Environment Variables
- `GEMINI_API_KEY`: Your Google Gemini API key
- `PORT`: Port number (auto-set by most platforms)
- `FLASK_ENV`: Set to `production` for production

### Security Considerations
- ✅ Passwords are hashed using Werkzeug
- ✅ SQL injection prevention
- ✅ Input validation
- ✅ Session management

### Database
- SQLite database will be created automatically
- For production, consider using PostgreSQL or MySQL

## 📊 Monitoring & Maintenance

### Logs
- Check deployment platform logs for errors
- Monitor API usage and costs
- Set up alerts for downtime

### Updates
- Push changes to GitHub
- Most platforms auto-deploy from GitHub
- Test locally before pushing

## 🆘 Troubleshooting

### Common Issues

1. **"Module not found" errors**
   - Ensure `requirements.txt` is in root directory
   - Check Python version compatibility

2. **"API key not configured"**
   - Verify environment variable is set correctly
   - Check deployment platform settings

3. **Database errors**
   - Ensure write permissions for database file
   - Consider using external database for production

4. **Port issues**
   - Use `os.environ.get('PORT', 3000)` for dynamic port assignment
   - Check platform-specific port configurations

### Support
- Check deployment platform documentation
- Review Flask deployment guides
- Monitor application logs

## 🎉 Success!

Once deployed, your AI Quiz Generator will be accessible to anyone with an internet connection!

**Features available online:**
- ✅ User registration and login
- ✅ AI-powered quiz generation
- ✅ Live leaderboard
- ✅ Personal result tracking
- ✅ Modern web interface

---

**Happy Deploying! 🚀** 