# Job Application Tracker – CRUD API

A production-ready backend REST API to manage and track job applications efficiently.  
This project provides full CRUD functionality along with analytics to monitor application status.

---

## 🚀 Features
- Create, read, update, and delete job applications
- Track application status (Applied, Interview, Offer, Rejected)
- Analytics endpoint to summarize job status counts
- Input validation with clear error responses
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

## 🌐 Live Demo
- **Base URL:**  
  https://job-application-tracker-quvt.onrender.com

- **Swagger API Documentation:**  
  https://job-application-tracker-quvt.onrender.com/docs

---

## 📌 API Endpoints

### Job Management
- `GET /jobs` – Fetch all job applications  
- `POST /jobs` – Add a new job application  
- `PUT /jobs/{id}` – Update an existing job  
- `DELETE /jobs/{id}` – Delete a job application  

### Analytics
- `GET /analytics/status-count` – Get count of applications by status  

---

## 📥 Sample Request (POST /jobs)

```json
{
  "company": "Google",
  "role": "Backend Developer",
  "status": "Applied",
  "applied_date": "2026-02-07"
}

---

## 🧪 How to Run Locally

```bash
# Clone the repository
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

Author:
Anusha K A
