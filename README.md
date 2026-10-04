# 🚀 CareerCopilotAI

> **An AI-powered career copilot that analyzes your resume, identifies skill gaps, and helps you prepare for your target role.**

[![Authentication](https://img.shields.io/badge/Authentication-Complete-brightgreen)](https://github.com/SREELAKSHMI079/CareerCopilotAI)
[![Resume Processing](https://img.shields.io/badge/Resume%20Processing-Complete-brightgreen)](https://github.com/SREELAKSHMI079/CareerCopilotAI)
[![Skill Gap Analysis](https://img.shields.io/badge/Skill%20Gap%20Analysis-Complete-brightgreen)](https://github.com/SREELAKSHMI079/CareerCopilotAI)
[![AI Analysis](https://img.shields.io/badge/AI%20Analysis-Complete-brightgreen)](https://github.com/SREELAKSHMI079/CareerCopilotAI)
[![RAG](https://img.shields.io/badge/RAG-Complete-brightgreen)](https://github.com/SREELAKSHMI079/CareerCopilotAI)
[![Career Guidance](https://img.shields.io/badge/Career%20Guidance-Complete-brightgreen)](https://github.com/SREELAKSHMI079/CareerCopilotAI)
[![Job Matching](https://img.shields.io/badge/Job%20Matching-Planned-lightgrey)](https://github.com/SREELAKSHMI079/CareerCopilotAI)
[![Interview Coach](https://img.shields.io/badge/Interview%20Coach-Planned-lightgrey)](https://github.com/SREELAKSHMI079/CareerCopilotAI)
[![Frontend](https://img.shields.io/badge/Frontend-Planned-lightgrey)](https://github.com/SREELAKSHMI079/CareerCopilotAI)
[![Deployment](https://img.shields.io/badge/Deployment-Planned-lightgrey)](https://github.com/SREELAKSHMI079/CareerCopilotAI)

---

## 🎯 What is CareerCopilotAI?

CareerCopilotAI is being built as a personal AI career assistant.

It takes your:

**Resume + Target Role**

and turns them into:

**Skill Analysis → Skill Gaps → AI Insights → Personalized Career Guidance**

The long-term goal is to evolve it into a complete career intelligence platform that can help with **job matching, learning roadmaps, resume optimization, interview preparation, and career planning.**

---

## ✨ Features

### 🔐 Authentication
- User registration
- Secure password hashing
- JWT authentication
- OAuth2
- Protected endpoints
- User-specific data access

### 📄 Resume Processing
- PDF resume upload
- PDF text extraction
- Resume storage in PostgreSQL
- Multiple resumes per user
- Resume ownership validation

### 🎯 Resume & Skill Analysis
- Target-role based analysis
- Role-specific skill requirements
- Resume skill detection
- Missing skill detection
- Skill-gap recommendations
- Regex-based whole-word skill matching

### 🤖 AI Resume Analysis
Powered by **Google Gemini**.

Provides:
- Candidate profile summary
- Relevant strengths
- Areas for improvement
- Role-specific feedback
- Resume improvement suggestions

### 🧠 RAG-Powered Career Guidance
CareerCopilotAI uses **Retrieval-Augmented Generation** to provide knowledge-grounded guidance for missing skills.

```text
Resume
   ↓
Skill Gap Analysis
   ↓
Missing Skills
   ↓
Semantic Retrieval
   ↓
Qdrant
   ↓
Relevant Career Knowledge
   ↓
Gemini
   ↓
Personalized Guidance
```
### 🔎 RAG Pipeline

```text
Career Knowledge
      ↓
Chunking
      ↓
Sentence Transformers
      ↓
Embeddings
      ↓
Qdrant
      ↓
Semantic Search
      ↓
Gemini
      ↓
Career Guidance
```
## 🛠️ Tech Stack

| Category            | Technologies                  |
|---------------------|-------------------------------|
| Backend             | Python, FastAPI               |
| Database            | PostgreSQL, SQLAlchemy        |
| Authentication      | JWT, OAuth2, Passlib, bcrypt  |
| AI                  | Google Gemini                 |
| RAG                 | Sentence Transformers, Qdrant |
| Embeddings          | `all-MiniLM-L6-v2`            |
| Document Processing | PyPDF                         |
| Development         | Git, GitHub, Uvicorn          |

## 🏗️ Current Architecture

```text
                         CareerCopilotAI
                                │
                                ▼
                           FastAPI
                                │
              ┌─────────────────┼─────────────────┐
              │                 │                 │
              ▼                 ▼                 ▼
       Authentication      Resume Processing   PostgreSQL
                                │
                                ▼
                         Skill Analysis
                                │
                                ▼
                          Skill Gaps
                                │
                    ┌───────────┴───────────┐
                    ▼                       ▼
                   RAG                  Gemini AI
                    │                       │
                    ▼                       │
                 Qdrant                     │
                    │                       │
                    └───────────┬───────────┘
                                ▼
                       Career Guidance
```

## 📂 Project Structure

```text
CareerCopilotAI/
│
├── main.py
├── models.py
├── schemas.py
├── database.py
├── auth.py
├── ai_service.py
├── role_skills.py
│
├── rag/
│   ├── documents/
│   │   └── career_skills.txt
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retrieve.py
│   ├── generate.py
│   └── rag_service.py
│
├── uploads/
│
├── .env
├── .gitignore
└── README.md
```
## 🔌 API

### Authentication

```text
POST /register
POST /login
GET  /me
```

### Resume

```text
POST /resume/upload
POST /resume/analyze/{resume_id}
```

The resume analysis endpoint currently combines:

```text
Resume Processing
       +
Skill Matching
       +
Skill Gap Analysis
       +
RAG Guidance
       +
Gemini AI Analysis
```
# 🗺️ Roadmap

### ✅ Completed

- [x] FastAPI backend
- [x] PostgreSQL integration
- [x] SQLAlchemy models
- [x] User registration
- [x] Password hashing
- [x] JWT authentication
- [x] OAuth2
- [x] Protected endpoints
- [x] Resume PDF upload
- [x] PDF text extraction
- [x] Resume storage
- [x] Multiple resume support
- [x] Role-based skill mapping
- [x] Resume skill matching
- [x] Skill-gap detection
- [x] Basic recommendations
- [x] Gemini AI resume analysis
- [x] RAG knowledge base
- [x] Document chunking
- [x] Sentence Transformer embeddings
- [x] Qdrant vector database
- [x] Semantic retrieval
- [x] Gemini RAG generation
- [x] RAG integration with resume analysis
- [x] Skill-specific career guidance

### 🚧 Next

- [ ] Job Description Matching
- [ ] Resume ↔ Job Match Score
- [ ] Job-specific Skill Gap Analysis
- [ ] Personalized Learning Roadmap
- [ ] Resume Optimization for Job Descriptions
- [ ] AI Interview Coach
- [ ] Multi-turn Interview Conversations

### 🔮 Future

- [ ] React Frontend
- [ ] User Career Dashboard
- [ ] Docker
- [ ] Cloud Deployment
- [ ] Production Monitoring

## 🚀 Long-Term Vision

CareerCopilotAI will evolve from a **resume analyzer** into a complete **AI career copilot**.

```text
              Resume
                 ↓
          Skill Analysis
                 ↓
            Skill Gaps
                 ↓
          Career Guidance
                 ↓
          Job Matching
                 ↓
      Personalized Roadmap
                 ↓
         Resume Optimization
                 ↓
        Interview Preparation
                 ↓
          Career Strategy
```

The eventual goal is to build an AI system that understands:

**Where you are → Where you want to go → What's missing → What to do next**

---

## 🔒 Security

The following are excluded from version control:

```text
.env
venv/
uploads/
rag/qdrant_data/
__pycache__/
.DS_Store
```

API keys, uploaded resumes, and local vector database data are not committed to GitHub.

---

## 👩‍💻 Author

**Sreelakshmi A**

B.Tech Computer Science Engineering  
Specialization: Artificial Intelligence & Machine Learning

---

⭐ **CareerCopilotAI — Building an AI-powered career copilot, one milestone at a time.**
