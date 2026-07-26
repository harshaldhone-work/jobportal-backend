from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="myJobApp", description="A simple job listing API built with FastAPI.", version="0.1.0")

class Job(BaseModel):
    id: int
    title: str
    company: str
    location: str
    description: str

jobs_db: List[Job] = [
    Job(id=1, title="Backend Developer", company="Acme Corp", location="Remote", description="Build and maintain APIs."),
    Job(id=2, title="Frontend Developer", company="Beta Inc", location="New York, NY", description="Create engaging user interfaces."),
]

@app.get("/", summary="API root")
def read_root() -> dict:
    return {"message": "Welcome to myJobApp! Visit /docs for the API docs."}

@app.get("/health", summary="Health check")
def health_check() -> dict:
    return {"status": "ok"}

@app.get("/jobs", response_model=List[Job], summary="List all jobs")
def list_jobs() -> List[Job]:
    return jobs_db

@app.get("/jobs/{job_id}", response_model=Job, summary="Get a job by ID")
def get_job(job_id: int) -> Job:
    job = next((job for job in jobs_db if job.id == job_id), None)
    if job is None:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Job not found")
    return job
