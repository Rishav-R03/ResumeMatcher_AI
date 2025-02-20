from fastapi import FastAPI
from pydantic import BaseModel 
from .backend.models import textProcess
from .backend.models.utils import parse_job_description
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Resume Matcher API is running"}

class JobDescription(BaseModel):
    text: str

@app.post("/parse_job")
def parse_job(request: JobDescription):
    return parse_job_description(request.text)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
