import sys
import os

# Add the parent folder to Python’s import path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fastapi import FastAPI, UploadFile, File
from orchestrator.router import Router
from orchestrator.fallback import FallbackHandler
import requests
import sys
import os

# Add the parent folder to Python’s import path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = FastAPI()
router = Router()
fallback = FallbackHandler()

@app.get("/")  # Define a root route for "/"
async def read_root():
    return {"message": "Welcome to the Multi-Agent Finance Assistant API!"}

@app.post("/ask/text")
async def ask_text(query: str):
    answer, confidence = router.handle_text_query(query)
    if confidence < 0.5:
        return {"response": fallback.clarify(), "confidence": confidence}
    return {"response": answer, "confidence": confidence}

@app.post("/ask/audio")
async def ask_audio(file: UploadFile = File(...)):
    file_path = f"/tmp/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())
    answer, confidence = router.handle_voice_input(file_path)
    if confidence < 0.5:
        return {"response": fallback.clarify(), "confidence": confidence}
    return {"response": answer, "confidence": confidence}
