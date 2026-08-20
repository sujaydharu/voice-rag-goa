from fastapi import FastAPI

app = FastAPI(
    title="Voice RAG Goa",
    description="Voice-enabled RAG system",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Voice RAG Goa API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }