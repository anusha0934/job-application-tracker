from sqlalchemy.orm import Session
from app import models

def job_status_count(db: Session):
    return (
        db.query(models.Job.status, models.Job.id)
        .all()
    )