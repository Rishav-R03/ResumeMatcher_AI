from fastapi import FastAPI
from pydantic import BaseModel
from backend.models.utils import parse_job_description

app = FastAPI()

class JobDescriptionRequest(BaseModel):
    text: str

@app.get("/")
def homePage():
    return {"Job Description Parser": "Welcome to application"}

@app.post("/parse-job/")
def parse_job(request: JobDescriptionRequest):
    return parse_job_description(request.text)
