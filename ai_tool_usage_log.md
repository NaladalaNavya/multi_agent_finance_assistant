# 🤖 AI Tool Usage Log

This document records the use of AI models, libraries, and configurations within the Multi-Agent Finance Assistant project.

---

## 🧠 Embeddings

- **Model**: `all-MiniLM-L6-v2`
- **Toolkit**: SentenceTransformers
- **Purpose**: Convert financial text and news filings into embeddings for semantic search
- **Output**: 384-dimensional vectors indexed in FAISS

## 🔍 Retrieval

- **Vector Store**: FAISS (FlatL2 index)
- **Search Method**: Top-k cosine similarity retrieval
- **Fallback Handling**: If `retrieval confidence < 0.5`, trigger clarification prompt via FallbackAgent

## 📝 Language Generation

- **Model**: `mistralai/Mistral-7B-Instruct-v0.1`
- **Library**: HuggingFace Transformers
- **Purpose**: Generate natural language briefs from retrieved documents and financial metrics

## 🔈 Voice I/O

- **STT (Speech to Text)**: `openai/whisper` base model
- **TTS (Text to Speech)**: `pyttsx3` (offline engine)
- **Pipeline**: Audio Input → Whisper STT → LLM → pyttsx3 Output

---

## 🧩 Agent-to-Tool Mapping

| Agent          | AI Tool/Model     | Role                                 |
| -------------- | ----------------- | ------------------------------------ |
| RetrieverAgent | MiniLM + FAISS    | Top-k vector-based semantic search   |
| LanguageAgent  | Mistral-7B        | Market brief generation              |
| VoiceAgent     | Whisper + pyttsx3 | Voice input/output                   |
| AnalysisAgent  | Rule-based        | Computes exposure, compares earnings |

---

## ✅ Open-Source Only

All AI tools used in this project are open, auditable, and deployable without proprietary licenses. No commercial APIs or closed models are used.
