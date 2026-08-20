from pydantic import BaseModel
from typing import List, Optional


class Source(BaseModel):
    document_id: Optional[str] = None
    text: str
    score: Optional[float] = None
    metadata: Optional[dict] = None


class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    transcript: Optional[str] = None
    answer: str
    sources: List[Source] = []
    confidence: Optional[float] = None
    grounded: Optional[bool] = None
    latency_ms: Optional[float] = None