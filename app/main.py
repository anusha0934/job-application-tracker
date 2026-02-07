from fastapi import FastAPI, Depends , HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, models 
from app.database import SessionLocal, engine
from app.models import Base
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job Application Tracker API")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Job Application Tracker API is running"}

@app.post("/jobs", response_model=schemas.JobResponse)
def add_job(job: schemas.JobCreate, db: Session = Depends(get_db)):
    return crud.create_job(db, job)

@app.get("/jobs", response_model=list[schemas.JobResponse])
def list_jobs(db: Session = Depends(get_db)):
    return crud.get_jobs(db)

@app.put("/jobs/{job_id}", response_model=schemas.JobResponse)
def update_job(
    job_id: int,
    job: schemas.JobCreate,
    db: Session = Depends(get_db)):
    return crud.update_job(db, job_id, job)

@app.delete("/jobs/{job_id}")
def delete_job(
    job_id: int,
    db: Session = Depends(get_db)
):
    return crud.delete_job(db, job_id)

@app.get("/analytics/status-count")
def status_count(db: Session = Depends(get_db)):
    jobs = db.query(models.Job).all()

    result = {}

    for job in jobs:
        if job.status in result:
            result[job.status] += 1
        else:
            result[job.status] = 1

    return result




    return new_user