from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from openai import OpenAI
import json
from datetime import datetime

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()
LOG_FILE = "logs.json"

class Query(BaseModel):
    question: str

def log_interaction(question, answer):
    entry = {
        "timestamp": str(datetime.utcnow()),
        "question": question,
        "answer": answer
    }
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([], f)
    data = json.load(open(LOG_FILE))
    data.append(entry)
    json.dump(data, open(LOG_FILE, "w"), indent=2)

@app.post("/ask")
def ask_question(payload: Query):
    question = payload.question.strip()
    prompt = f"""
    You are an LED manufacturing expert.
    Provide deep practical insight (driver failures, SMT, reflow, optics, thermal).

    QUESTION: {question}

    Keep it specific and technical.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    answer = response.choices[0].message["content"]
    log_interaction(question, answer)
    return {"answer": answer}
