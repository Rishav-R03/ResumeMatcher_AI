# 🔍 AI-Powered Resume & Job Matcher

## 🚀 Overview
This project is an **AI-powered Resume & Job Matching System** that utilizes **FastAPI**, **LangChain**, **OpenAI (Gemini)**, **Elasticsearch**, **PostgreSQL**, and **Streamlit**. It provides **automated resume parsing, job description analysis, and AI-driven candidate-job matching**.

Additionally, it integrates a **Resume Parser** that takes resumes in PDF format, extracts key details, and matches them with job descriptions. It provides two outputs:
1. **Structured information** about the resume based on the job description.
2. **Percentage match** between the resume and the job description.

---

## 🎯 Features
### ✅ Core Features
- **Resume Parsing**: Extract skills, experience, education from PDFs.
- **Job Description Parsing**: Extract relevant keywords and skills.
- **AI-Powered Matching**: Rank resumes against job descriptions.
- **Job Recommendations**: Suggest jobs based on resume content.
- **Real-time Search**: Use Elasticsearch for fast and relevant search.

### 🌟 Bonus Features
- **ATS-Friendly Parsing**: Improve candidate ranking using AI.
- **Resume Storage & Retrieval**: Save and fetch resumes efficiently.
- **Percentage Matching**: AI computes resume-job match percentage.
- **Cloud Deployment**: Runs seamlessly on AWS/GCP.

---

## 🏗️ Tech Stack
| **Component**  | **Technology** |
|--------------|--------------|
| **Backend**  | FastAPI |
| **Frontend** | Streamlit |
| **Database** | PostgreSQL |
| **Search Engine** | Elasticsearch |
| **AI Models** | OpenAI Gemini, LangChain |
| **Cloud Storage** | AWS S3 |
| **Deployment** | Docker, Kubernetes |

---

## 🛠️ Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/resume-job-matcher.git
cd resume-job-matcher
```

### 2️⃣ Set Up Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Start Backend (FastAPI)
```sh
uvicorn main:app --reload
```

### 5️⃣ Start Frontend (Streamlit)
```sh
streamlit run frontend/app.py
```

---

## 📂 Project Structure
```
📦 resume-job-matcher
├── 📂 backend
│   ├── main.py  # FastAPI main file
│   ├── models.py  # Database models
│   ├── parsers.py  # Resume & job parsing logic
│   ├── matcher.py  # AI matching logic
│   ├── database.py  # PostgreSQL connection
│   ├── utils.py  # Helper functions
│   └── requirements.txt  # Backend dependencies
│
├── 📂 frontend
│   ├── app.py  # Streamlit UI
│   └── requirements.txt  # Frontend dependencies
│
├── 📂 data
│   ├── resumes/  # Sample resumes (PDFs)
│   ├── job_descriptions/  # Sample job descriptions
│
├── 📜 README.md  # Project documentation
└── 📜 Dockerfile  # Containerization setup
```

---

## 🚀 API Endpoints
### **Resume Parsing API**
**Endpoint:** `POST /parse-resume/`
**Request:**
```json
{
  "resume": "(PDF File Upload)",
  "job_description": "Senior Backend Engineer with Python experience."
}
```
**Response:**
```json
{
  "extracted_info": {
    "name": "John Doe",
    "skills": ["Python", "FastAPI", "Docker"],
    "experience": "5 years in backend development"
  },
  "match_percentage": "85%"
}
```

### **Job Description Parsing API**
**Endpoint:** `POST /parse-job/`
**Request:**
```json
{
  "text": "We are looking for a Senior Python Developer with experience in FastAPI and Kubernetes."
}
```
**Response:**
```json
{
  "keywords": ["Python", "FastAPI", "Kubernetes"],
  "entities": {
    "job_titles": ["Senior Python Developer"],
    "skills": ["FastAPI", "Kubernetes"]
  }
}
```

---

## 🌍 Deployment
### **Run with Docker**
```sh
docker build -t resume-matcher .
docker run -p 8000:8000 resume-matcher
```

### **Deploy to Kubernetes**
```sh
kubectl apply -f k8s-deployment.yaml
```

### **CI/CD with GitHub Actions**
Add a `.github/workflows/deploy.yml` file to automate testing and deployment.

---

## 🛠️ Future Improvements
- 🔹 Fine-tune AI models for better resume-job matching.
- 🔹 Improve ATS parsing compatibility.
- 🔹 Implement user authentication for secure resume storage.

---

## 🎯 Contributors
- **Your Name** - [GitHub](https://github.com/your-username)

---

## 📜 License
This project is licensed under the MIT License.

---

### 🎉 Ready to Match Resumes with Jobs?
Run the app and start parsing resumes & job descriptions in seconds! 🚀

