# 📈 Multi-Agent Finance Assistant

An open-source, voice-enabled RAG-based system that delivers daily market briefs using specialized agents. The assistant performs API ingestion, semantic retrieval, LLM-based synthesis, and voice interaction — all orchestrated via microservices.

---

## 🧪 Use Case: Morning Market Brief

> At 8 AM, a portfolio manager asks:  
> “What’s our risk exposure in Asia tech stocks today, and highlight any earnings surprises?”

**Response Example**:

> “Your Asia tech allocation is 22%, up from 18% yesterday.  
> TSMC beat estimates by 4%, Samsung missed by 2%.  
> Sentiment is neutral with a cautionary tilt due to rising yields.”

---

## 🏗️ System Architecture-

```mermaid
graph TD
    A[Voice Input (Mic/Upload)] --> B[Whisper STT]
    B --> C[Intent Recognition]
    C --> D[API Ingestion Agent]
    D --> E[Semantic Retrieval Agent]
    E --> F[LLM-based Synthesis]
    F --> G[Voice Output]

```
