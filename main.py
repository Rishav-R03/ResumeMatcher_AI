from fastapi import FastAPI
from pydantic import BaseModel
from backend.models.utils import extract_entities_gemini

app = FastAPI()

class JobDescriptionRequest(BaseModel):
    text: str

@app.get("/")
def homePage():
    return {"Job Description Parser": "Welcome to application"}

@app.post("/parse-job/")
async def parse_job(request: JobDescriptionRequest):
    result = {
        "job_titles": ["Senior DevOps Engineer"],
        "skills": ["AWS", "Kubernetes", "Terraform"],
        "experience_level": ["Senior"]
    }
    return result
