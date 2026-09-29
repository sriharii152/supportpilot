# SupportPilot

## Memory-Powered Customer Support Agent

SupportPilot is an AI-powered customer support agent that uses persistent customer-specific memory to provide more personalized and context-aware support.

Instead of asking customers to repeatedly explain their technical environment and previous issues, SupportPilot recalls relevant information from previous interactions and uses it when generating new responses.

---

# Problem

Traditional AI support agents can behave like stateless assistants.

For example, a customer may previously explain:

- Programming language
- API version
- Database
- Previous incident
- Root cause
- Successful solution
- Support preferences

When the customer starts a new conversation, the agent may ask the same questions again.

This creates unnecessary friction.

---

# Solution

SupportPilot uses Hindsight as a persistent memory layer.

The system follows:

Retain → Recall → Generate → Retain

When a customer provides useful information, it is retained in Hindsight.

When the customer starts another interaction, relevant memories are recalled and provided to the LLM.

The LLM then generates a personalized support response.

---

# Architecture

Customer
↓
Frontend
↓
FastAPI Backend
↓
Hindsight Memory + Groq LLM
↓
Personalized Response

---

# Technology Stack

## Frontend

- HTML
- CSS
- JavaScript

## Backend

- Python
- FastAPI
- Uvicorn

## AI

- Groq
- Llama model

## Memory

- Hindsight
- Retain
- Recall

---

# Core Features

## 1. Persistent Customer Memory

Stores customer-specific support information.

## 2. Contextual Recall

Retrieves relevant information for a new support request.

## 3. Personalized Responses

Uses recalled information to generate more relevant responses.

## 4. Memory ON/OFF

Allows comparison between a stateless and memory-powered response.

## 5. Customer Isolation

Each customer receives a separate memory bank.

---

# Demo Customer

Rahul Sharma

Company:
AcmeCloud

Role:
Backend Engineer

Environment:

- Node.js
- API v2
- PostgreSQL

Previous issue:

API timeout caused by insufficient database connection pool size.

Previous solution:

Connection pool increased from 10 to 30.

---

# Example

Without memory:

Customer:

"My API is timing out again."

Agent:

"What API version are you using?
What environment are you running?
What happened previously?"

With memory:

Customer:

"My API is timing out again."

SupportPilot:

"I remember your Node.js/API v2 environment. Last time your API timeout was related to the connection pool. Let's first check whether the same condition has returned."

---

# Hindsight Integration

SupportPilot uses two primary Hindsight operations:

## Retain

Stores useful customer information.

## Recall

Retrieves information relevant to the current customer request.

The basic workflow is:

Retain
↓
Customer Memory
↓
Recall
↓
LLM
↓
Response
↓
Retain

---

# Project Structure

supportpilot/

backend/
- main.py
- agent.py
- memory.py
- prompts.py
- config.py
- requirements.txt

frontend/
- index.html
- style.css
- script.js

demo/
- demo-data.json

---

# Installation

Clone the repository.

Create a virtual environment:

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

Install dependencies:

pip install -r backend/requirements.txt

---

# Environment Variables

Create:

backend/.env

Add:

GROQ_API_KEY=your_key
HINDSIGHT_API_KEY=your_key
HINDSIGHT_BASE_URL=https://api.hindsight.vectorize.io

Never commit API keys to GitHub.

---

# Run Backend

Open terminal:

cd backend

Run:

uvicorn main:app --reload

Backend:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs

---

# Run Frontend

Open another terminal:

cd frontend

Run:

python -m http.server 5500

Open:

http://127.0.0.1:5500

---

# Demo

1. Start the backend.
2. Open FastAPI documentation.
3. Run `/demo/seed`.
4. Open the SupportPilot frontend.
5. Turn Memory OFF.
6. Ask:

"My API is timing out again."

7. Observe the generic response.
8. Turn Memory ON.
9. Ask the same question.
10. Observe the personalized response.
11. View recalled information in the Hindsight Memory panel.

---

# Limitations

This prototype focuses on demonstrating persistent customer memory.

It does not currently include:

- Production authentication
- Multi-tenant enterprise security
- Human support escalation
- Advanced analytics
- Production deployment
- Large-scale monitoring

These can be added in future versions.

---

# Future Improvements

- Human agent handoff
- Customer sentiment tracking
- Support ticket integration
- Knowledge-base integration
- Multi-agent support workflows
- Analytics dashboard
- Enterprise authentication
- Memory quality evaluation

---

# Safety

The application should never expose API keys in frontend code.

Environment variables are used for credentials.

Customer data should be protected appropriately before production deployment.