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
def parse_job(request: JobDescriptionRequest):
    return extract_entities_gemini(request.text)
