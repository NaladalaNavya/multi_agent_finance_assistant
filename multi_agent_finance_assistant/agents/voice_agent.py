import whisper
import pyttsx3

class VoiceAgent:
    def __init__(self):
        self.model = whisper.load_model("base")
        self.tts_engine = pyttsx3.init()

    def speech_to_text(self, audio_path: str):
        result = self.model.transcribe(audio_path)
        return result["text"]

    def text_to_speech(self, text: str):
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()
