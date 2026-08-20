# System Architecture

## End-to-End Pipeline

User
↓
Frontend
↓
Speech-to-Text
↓
Query
↓
Query Embedding
↓
Vector Database
↓
Top-K Retrieval
↓
Retrieved Context
↓
RAG Harness
↓
Guardrails
↓
LLM
↓
Structured Response
↓
Frontend

## Module Ownership

### Member 1
Data + RAG

### Member 2
Voice + AI

### Member 3
Frontend + API + Performance + Deployment