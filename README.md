# 📌 Job Application Tracker – CRUD API

A production-ready backend REST API to manage and track job applications efficiently.  
This project provides full CRUD functionality along with analytics to monitor application status.

---

## 🧩 Problem Statement

Managing job applications manually using notes, spreadsheets, or emails often leads to poor organization, missed follow-ups, and lack of visibility into application progress.

Common challenges include:
- No centralized system for tracking applications
- Difficulty updating and monitoring application status
- No analytics or summary of job outcomes

There is a need for a structured, scalable solution to manage job applications effectively.

---

## 💡 Solution Overview

The **Job Application Tracker – CRUD API** is a backend service built using **FastAPI** that enables users to store, manage, update, and analyze job applications through RESTful endpoints.

The system provides:
- Complete CRUD operations for job applications
- Status tracking (Applied, Interview, Offer, Rejected)
- Analytics endpoints to summarize application data
- Input validation with meaningful error responses
- Auto-generated API documentation using Swagger
- Cloud deployment for public access

This solution is lightweight, scalable, and suitable for real-world usage.

---

## ✨ Features

- Create, read, update, and delete job applications
- Track application status (Applied, Interview, Offer, Rejected)
- Analytics endpoint to count applications by status
- Input validation using Pydantic
- Clear and structured error handling
- Automatically generated API documentation
- Deployed and accessible online

---

## 🛠️ Tech Stack

- **Backend Framework:** FastAPI  
- **Language:** Python  
- **Database:** SQLite  
- **ORM:** SQLAlchemy  
- **Deployment:** Render  
- **API Docs:** Swagger (OpenAPI)

---

## 🔄 Project Workflow

1. Client sends an API request (POST / GET / PUT / DELETE)
2. FastAPI validates request data using Pydantic models
3. Business logic processes the request
4. SQLAlchemy performs database operations
5. JSON response is returned to the client
6. Analytics endpoints aggregate application data by status
7. Interactive API documentation is available via `/docs`

This workflow ensures clean architecture, reliable data handling, and easy extensibility.

---

## 🚀 Live Demo

- **Base URL:**  
  https://job-application-tracker-<id>.onrender.com

- **Swagger API Docs:**  
  https://job-application-tracker-<id>.onrender.com/docs

- **Analytics Endpoint:**  
  https://job-application-tracker-<id>.onrender.com/analytics/status-count
  
---

## 📌 API Endpoints (Summary)

| Method | Endpoint | Description |
|------|--------|-------------|
| GET | `/jobs` | Get all job applications |
| POST | `/jobs` | Create a new job application |
| GET | `/jobs/{id}` | Get job by ID |
| PUT | `/jobs/{id}` | Update job application |
| DELETE | `/jobs/{id}` | Delete job application |
| GET | `/analytics/status-count` | Get job count by status |

---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/anusha0934/job-application-tracker.git

# Navigate to the project
cd job-application-tracker

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app.main:app --reload

Open your browser:
http://127.0.0.1:8000/docs

---

Project Structure:

job-application-tracker/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│
├── analytics/
├── requirements.txt
├── README.md
└── jobs_tracker.db

---

## Future Enhancements:

-User authentication and authorization
-Migration from SQLite to PostgreSQL
-Interview reminders and notifications
-Advanced analytics dashboards
-Frontend integration (React / Angular)
-Resume and document upload
-Automated testing (unit & integration tests)

--- 

## Author:
  Anusha K A

