# Voice RAG Goa

Voice-enabled Retrieval-Augmented Generation system for the HH Goa 2026 hackathon.

## Pipeline

Voice
↓
Speech-to-Text
↓
Query Processing
↓
Embedding
↓
Vector Database
↓
Retrieval
↓
RAG Harness
↓
Guardrails
↓
LLM
↓
Answer

## Team Responsibilities

### Member 1 — Data + RAG
- Dataset
- Preprocessing
- Chunking
- Embeddings
- Vector database
- Retrieval

### Member 2 — AI + Voice
- Speech-to-text
- LLM
- Prompt engineering
- Harness
- Guardrails
- Error handling

### Member 3 — Application + Performance
- Frontend
- API integration
- Latency
- Testing
- Deployment

## Running Backend

```bash
pip install -r requirements.txt

uvicorn backend.main:app --reload
