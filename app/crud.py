from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import models, schemas


def create_job(db: Session, job: schemas.JobCreate):
    db_job = models.Job(
        company=job.company,
        role=job.role,
        status=job.status,
        applied_date=job.applied_date
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job


def get_jobs(db: Session):
    return db.query(models.Job).all()


def update_job(db: Session, job_id: int, job: schemas.JobCreate):
    db_job = db.query(models.Job).filter(models.Job.id == job_id).first()

    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")

    db_job.company = job.company
    db_job.role = job.role
    db_job.status = job.status
    db_job.applied_date = job.applied_date

    db.commit()
    db.refresh(db_job)
    return db_job


def delete_job(db: Session, job_id: int):
    job = db.query(models.Job).filter(models.Job.id == job_id).first()

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    db.delete(job)
    db.commit()
    return {"message": "Job deleted successfully"}


