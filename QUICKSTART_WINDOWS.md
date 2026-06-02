# 🚀 Quick Start Guide - Windows

## For Your Situation (Windows PowerShell User)

You received these errors:
```
- bash scripts/dev-setup.sh → Windows doesn't support bash natively
- make setup → make command not available
```

**Solution: Use the Windows batch script instead!**

---

## ⚡ Quick Setup (5 Minutes)

### Step 1: Open PowerShell as Administrator

Press `Win + X` → Choose "Windows PowerShell (Admin)"

### Step 2: Navigate to Project
```powershell
cd Homomorphic-Encryption-Tool-
```

### Step 3: Run Windows Setup
```powershell
.\scripts\setup-windows.bat
```

**That's it!** The script will:
- ✅ Check Docker & Node.js
- ✅ Setup environment variables
- ✅ Install dependencies
- ✅ Start all services

---

## 📍 What Gets Started

After running the script, you'll have:

| Service | URL | Purpose |
|---------|-----|---------|
| Frontend | http://localhost:3000 | Web Dashboard |
| Backend API | http://localhost:8000 | REST API |
| API Docs | http://localhost:8000/docs | Interactive API |
| PostgreSQL | localhost:5432 | Database |
| Redis | localhost:6379 | Cache |

---

## 🔐 Login Credentials

```
Email: test@secureml.com
Password: Test@1234
```

---

## ⚠️ Prerequisites (One-Time Setup)

### 1. Install Docker Desktop
- Download: https://www.docker.com/products/docker-desktop
- Install and restart your computer
- **Important**: Make sure WSL 2 is enabled

Verify:
```powershell
docker --version
# Output: Docker version 24.x.x, build xxxxx
```

### 2. Install Node.js
- Download: https://nodejs.org/ (LTS version recommended)
- Install and restart PowerShell
- Verify:
```powershell
node --version
# Output: v18.x.x or higher
```

### 3. Install Git
- Download: https://git-scm.com/
- Install
- Verify:
```powershell
git --version
# Output: git version 2.x.x
```

---

## 🎯 Common Commands (Windows PowerShell)

### Check services are running
```powershell
docker-compose ps
```

### View logs
```powershell
docker-compose logs -f
```

### Stop services
```powershell
docker-compose down
```

### Start services again
```powershell
docker-compose up -d
```

### Start frontend dev server (new terminal)
```powershell
cd frontend
npm run dev
```

### Test API
```powershell
curl http://localhost:8000/health
```

---

## ❌ Troubleshooting

### Problem: "Docker is not recognized"
```powershell
# Docker Desktop may need restart
# Option 1: Restart your computer
# Option 2: Restart Docker Desktop application
# Option 3: Close and reopen PowerShell

docker --version
```

### Problem: "Port 3000/8000 already in use"
```powershell
# Stop all services
docker-compose down

# Wait a few seconds, then restart
docker-compose up -d
```

### Problem: "Database connection error"
```powershell
# Restart PostgreSQL
docker-compose restart postgres

# Check logs
docker-compose logs postgres
```

### Problem: "npm packages failed to install"
```powershell
cd frontend

# Delete old files
Remove-Item -Recurse node_modules
Remove-Item package-lock.json

# Reinstall
npm install

cd ..
```

### Problem: "Access denied" when running batch file
```powershell
# Run PowerShell as Administrator
# Right-click PowerShell → Run as Administrator

# Then navigate and try again
.\scripts\setup-windows.bat
```

---

## 📚 Full Documentation

For more detailed guides, see:

| Document | Purpose |
|----------|---------|
| [WINDOWS_SETUP.md](./docs/WINDOWS_SETUP.md) | Complete Windows setup guide |
| [README.md](./README.md) | Main project overview |
| [DEPLOYMENT.md](./docs/DEPLOYMENT.md) | Production deployment |
| [API.md](./docs/API.md) | API reference |
| [ARCHITECTURE.md](./docs/ARCHITECTURE.md) | System design |

---

## 🎨 Using the Dashboard

### Login
1. Open http://localhost:3000
2. Enter test credentials
3. Click "Sign In"

### Dashboard Features
- 📊 View statistics and charts
- 📤 Upload ML models
- 🔮 Make encrypted predictions
- 🔑 Manage encryption keys
- ⚙️ Account settings

### Upload a Model
1. Go to "Models" page
2. Click "Upload Model"
3. Fill in details:
   - Model Name
   - Description
   - Model Type (e.g., Linear Regression)
   - Input Features (number of inputs)
   - Output Type (regression/classification)
4. Select model file (.joblib, .pkl)
5. Click "Upload Model"

### Make a Prediction
1. Go to "Predictions" page
2. Click "New Prediction"
3. Select a model
4. Enter encrypted input data
5. Click "Run Prediction"

---

## 🔧 Development Tips

### Using VS Code (Recommended)
1. Download: https://code.visualstudio.com/
2. Open project: `code .`
3. Install extensions:
   - Python
   - FastAPI
   - ES7+ React/Redux/React-Native snippets
   - Tailwind CSS IntelliSense

### Debug Backend
Create `.vscode/launch.json` to debug Python code

### Test API with Thunder Client
- In VS Code: Install "Thunder Client" extension
- Make API requests without curl
- Easier than PowerShell commands

---

## 📦 Project Structure

```
Homomorphic-Encryption-Tool-/
├── backend/                    # Python FastAPI
│   ├── app/                    # Application code
│   ├── requirements.txt        # Dependencies
│   ├── Dockerfile              # Container
│   └── .env.example            # Environment template
│
├── frontend/                   # Next.js React
│   ├── src/                    # Application code
│   ├── package.json            # Dependencies
│   └── README.md               # Frontend docs
│
├── scripts/
│   ├── setup-windows.bat       # ⭐ Windows setup
│   ├── dev-setup.sh            # Linux/Mac setup
│   ├── init_db.py              # Database init
│   └── create_sample_data.py   # Sample data
│
├── docs/                       # Documentation
│   ├── WINDOWS_SETUP.md        # Windows guide
│   ├── DEPLOYMENT.md           # Deployment guide
│   ├── API.md                  # API reference
│   └── ARCHITECTURE.md         # System design
│
├── docker-compose.yml          # Services config
├── Makefile                    # Tasks (Linux/Mac)
├── .gitignore                  # Git ignore rules
└── README.md                   # Main README
```

---

## 🚀 Next Steps

### After Setup:
1. ✅ Access http://localhost:3000
2. ✅ Login with test credentials
3. ✅ Explore the dashboard
4. ✅ Check API docs at http://localhost:8000/docs
5. ✅ Read [ARCHITECTURE.md](./docs/ARCHITECTURE.md)

### When Ready to Deploy:
1. 📖 Read [DEPLOYMENT.md](./docs/DEPLOYMENT.md)
2. 🚀 Choose deployment option (Railway + Vercel recommended)
3. 📝 Configure production environment
4. 🌐 Deploy!

---

## 💡 Tips & Tricks

### Keep Docker Running
- Don't close PowerShell after running `docker-compose up -d`
- Docker runs in background automatically
- You can close the terminal

### Speed Up Development
- Use VS Code for editing
- Use browser DevTools for debugging
- Use Thunder Client for API testing
- Keep browser cache enabled

### Reset Everything
```powershell
# Stop and remove all data
docker-compose down -v

# Start fresh
.\scripts\setup-windows.bat
```

---

## ❓ Still Having Issues?

### Check Docker is Running
```powershell
# Docker Desktop must be running
# Look for Docker icon in system tray
# If not there, open Docker Desktop application
```

### Check Ports are Free
```powershell
# In PowerShell as Administrator:
netstat -ano | findstr :3000
netstat -ano | findstr :8000
netstat -ano | findstr :5432
# If ports show "LISTENING", close those applications
```

### View All Logs
```powershell
# Full logs from all services
docker-compose logs

# Specific service logs
docker-compose logs backend
docker-compose logs postgres
docker-compose logs redis
```

### Get Help
- 📖 Check documentation in `/docs` folder
- 🔗 Visit API docs at http://localhost:8000/docs
- 💬 Open GitHub issue: https://github.com/gangjinu/Homomorphic-Encryption-Tool-/issues
- 📧 Contact repository maintainer

---

## ✨ Success Checklist

- [ ] Docker Desktop installed and running
- [ ] Node.js installed (v18+)
- [ ] Repository cloned
- [ ] `setup-windows.bat` executed successfully
- [ ] Frontend accessible at http://localhost:3000
- [ ] Backend accessible at http://localhost:8000
- [ ] Can login with test credentials
- [ ] Can see dashboard with charts
- [ ] API documentation loading at http://localhost:8000/docs

**Once all boxes are checked, you're ready to start developing! 🎉**

---

**Happy Hacking! 🚀**
