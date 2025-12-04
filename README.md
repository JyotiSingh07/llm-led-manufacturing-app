# LED Manufacturing LLM App

This is a small AI-driven application that answers LED manufacturing-related questions using a Large Language Model (LLM).  
The project includes a **FastAPI backend** and a **React + Vite frontend**.

---

## 🚀 How to Run the Project (Local Setup)

---

# 1. Backend (FastAPI)

### Step 1: Setup virtual environment
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate     # Mac/Linux


#### Step 2: Install dependencies
pip install -r requirements.txt


#### Step 3: Set your OpenAI API Key  
cp .env.example .env
OPENAI_API_KEY=your_openai_api_key_here


#### Step 4: Start backend
uvicorn main:app --reload --port 8000


---

### 2. Frontend (React + Vite)

#### Step 1: Install dependencies
cd frontend
npm install


#### Step 2: Start frontend
npm start
Frontend runs at: http://localhost:3000



## 🧪 Test Backend with curl

curl -X POST "http://localhost:8000/ask" \
-H "Content-Type: application/json" \
-d '{"question": "Why do LED drivers fail thermal tests?"}'



---

## 📁 Project Structure

backend/
  main.py
  requirements.txt
  .env.example
  logs.json

frontend/
  src/
  index.html
  package.json
  vite.config.js

README.md


---

## ✔ Features
- Domain-specific LED manufacturing expertise using LLM  
- Clean FastAPI backend  
- React-based frontend with Vite  
- CORS enabled  
- Logging of queries & responses  
- Easy local setup  
