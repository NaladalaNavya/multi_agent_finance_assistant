from agents.api_agent import APIAgent
from agents.scraping_agent import ScrapingAgent
from agents.retriever_agent import RetrieverAgent
from agents.analysis_agent import AnalysisAgent
from agents.language_agent import LanguageAgent
from agents.voice_agent import VoiceAgent

class Router:
    def __init__(self):
        self.api_agent = APIAgent()
        self.scraper = ScrapingAgent()
        self.retriever = RetrieverAgent()
        self.analyzer = AnalysisAgent()
        self.language = LanguageAgent()
        self.voice = VoiceAgent()

    def handle_voice_input(self, audio_path: str):
        query = self.voice.speech_to_text(audio_path)
        return self.handle_text_query(query)

    def handle_text_query(self, query: str):
        retrieved_docs = self.retriever.retrieve(query)
        if not retrieved_docs:
            return None, 0.0  # Fallback condition
        narrative_prompt = f"Based on these docs: {retrieved_docs}, answer: {query}"
        response = self.language.generate_narrative(narrative_prompt)
        return response, 1.0
