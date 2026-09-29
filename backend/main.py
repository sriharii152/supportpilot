from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from agent import generate_response
from memory import retain_memory, recall_memory


app = FastAPI(
    title="SupportPilot API",
    description="Memory-Powered Customer Support Agent using Hindsight and Groq",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


class ChatRequest(BaseModel):
    customer_id: str
    customer_name: str
    message: str
    memory_enabled: bool = True


@app.get("/")
def home():
    return {
        "status": "online",
        "application": "SupportPilot",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    result = generate_response(
        customer_id=request.customer_id,
        customer_name=request.customer_name,
        message=request.message,
        memory_enabled=request.memory_enabled
    )

    return {
        "success": True,
        "answer": result["answer"],
        "memories": result["memories"],
        "memory_enabled": request.memory_enabled
    }


@app.post("/demo/seed")
def seed_demo_customer():

    customer_id = "rahul"

    customer_memory = """
Customer profile:

Name: Rahul Sharma

Company: AcmeCloud

Role: Backend Engineer

Technical environment:

- Node.js
- API v2
- PostgreSQL

Previous support incident:

Rahul experienced repeated API timeouts.

Root cause:

The database connection pool was too small.

Previous successful solution:

The connection pool was increased
from 10 connections to 30 connections.

Customer preference:

Rahul prefers not to repeat technical
information that he has already provided.
"""

    success = retain_memory(
        customer_id=customer_id,
        content=customer_memory
    )

    return {
        "success": success,
        "customer_id": customer_id,
        "message": "Rahul's support history has been stored in Hindsight."
    }


@app.get("/demo/memories")
def view_demo_memories():

    memories = recall_memory(
        customer_id="rahul",
        query="Show Rahul's technical environment, previous API timeout and successful fix."
    )

    return {
        "customer": "Rahul Sharma",
        "memories": memories
    }