from fastapi import FastAPI, UploadFile, File
from orchestrator.router import Router
from orchestrator.fallback import FallbackHandler

app = FastAPI()
router = Router()
fallback = FallbackHandler()

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
