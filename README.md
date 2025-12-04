# LED Manufacturing LLM App

Fully working assignment for Matrix Marketers.

## Backend (FastAPI)
- Python + FastAPI
- Single `/ask` endpoint using OpenAI API
- JSON logging
- Prompt engineered for LED manufacturing

## Frontend (React)
- Minimal UI
- Textbox + response display

## Setup Instructions

### Backend:
cd backend
pip install -r requirements.txt
cp .env.example .env  # Add OPENAI_API_KEY
uvicorn main:app --reload

### Frontend:
cd frontend
npm install
npm start
