# SupportZen 

### AI-Powered Luxury Retail Customer Service Chatbot.

SupportZen is a production-ready AI-powered customer service
backend designed for luxury fashion retail brands.\
It provides intelligent, scalable, and secure customer support using
Large Language Models (LLMs), RAG architecture, Redis memory, and a
modular multi-agent system.

------------------------------------------------------------------------

## 🚀 Key Features

-   Multi-Agent Architecture (Product, Order, Policy, Concierge)
-   RAG (Retrieval Augmented Generation)
-   Redis Session Memory
-   Database Integration (SQLAlchemy)
-   Secure API-based Architecture
-   Logging & Observability
-   Dockerized Deployment
-   FastAPI Backend
-   Production-Ready Structure

------------------------------------------------------------------------

## 🏗 Architecture Overview

SupportZen follows a layered enterprise architecture:

1.  Presentation Layer -- Website Chat UI\
2.  API Layer -- FastAPI Endpoints\
3.  Orchestration Layer -- Multi-Agent Router\
4.  AI Layer -- LLM Integration (OpenAI)\
5.  Retrieval Layer -- FAISS Vector Store\
6.  Memory Layer -- Redis\
7.  Database Layer -- SQLAlchemy ORM\
8.  Infrastructure Layer -- Docker

------------------------------------------------------------------------

## 📁 Project Structure

    supportzen
    │
    ├── app/
    │   ├── api/
    │   ├── agents/
    │   ├── services/
    │   ├── tools/
    │   ├── db/
    │   ├── core/
    │   ├── schemas/
    │   └── utils/
    │
    ├── data/
    ├── docker/
    ├── requirements.txt
    ├── .env
    └── run.py

------------------------------------------------------------------------

## ⚙️ Installation (Local Development)

### 1️⃣ Clone the Repository

    git clone: 
    cd supportzen_enterprise

### 2️⃣ Create Virtual Environment

    python -m venv venv

Activate:

Windows:

    venv\Scripts\activate

Mac/Linux:

    source venv/bin/activate

### 3️⃣ Install Dependencies

    pip install -r requirements.txt

### 4️⃣ Configure Environment Variables

Create `.env` file:

    OPENAI_API_KEY=your_openai_key
    DATABASE_URL=your_Database
    REDIS_URL=your_redis_url
    ENV= your_env

### 5️⃣ Run Application

    python run.py

Access Swagger UI: NA

------------------------------------------------------------------------

## 🐳 Docker Deployment

    docker-compose up --build

------------------------------------------------------------------------

## 📌 API Endpoints

### Health Check

GET /health

### Chat

POST /chat

Example Body: { "message": " please suggest me a panjabi for eid?", "respone": great, please check these product code "abc123", "yx123", "c58", "z423"
}

------------------------------------------------------------------------

## 🛠 Tech Stack

-   Python 3.11
-   FastAPI
-   LangChain
-   OpenAI API
-   FAISS
-   Redis
-   SQLAlchemy
-   Docker

------------------------------------------------------------------------

## 📄 License

Internal business use. Modify as needed.

## 👤 Author

**Abul Kalam Azad**
### Analyst and AI Developer 
---

⭐ If you like this project, give it a star on GitHub!

