from pydantic import BaseModel
class JobCreate(BaseModel):
    company: str
    role: str
    status: str
    applied_date: str

class JobResponse(JobCreate):
    id: int
class JobUpdate(BaseModel):
    status: str

    class Config:
        from_attributes = True

