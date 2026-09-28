import re

from fastapi import FastAPI, HTTPException, Depends, UploadFile, File
from pypdf import PdfReader
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from database import engine, Base, SessionLocal
import models
from schemas import UserCreate,UserLogin, ResumeAnalysisRequest
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import os
from models import User,Resume
from auth import (hash_password,verify_password,create_access_token,verify_access_token)
from role_skills import ROLE_SKILLS
Base.metadata.create_all(bind=engine)
app=FastAPI()
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@app.post("/register")
def register_user(user: UserCreate):
    db=SessionLocal()
    new_user=User(
        full_name=user.full_name,
        email=user.email,
        password_hash=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        "message":"REGISTRATION SUCCESSFULL"
    }
@app.post("/login")
def login_user(user: OAuth2PasswordRequestForm = Depends()):
    db=SessionLocal()
    existing_user = db.query(User).filter(User.email == user.username).first()
    if existing_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
    if not verify_password(
        user.password,
        existing_user.password_hash
    ):
        raise HTTPException(status_code=401,detail="Invalid email or password"
        )
    access_token=create_access_token(data={"sub": existing_user.email})
    return {
        "access_token":access_token,
        "token_type":"bearer"
    }
@app.get("/me")
def get_current_user(token: str = Depends(oauth2_scheme)):
    email = verify_access_token(token)

    db = SessionLocal()

    existing_user = db.query(User).filter(
        User.email == email
    ).first()


    if existing_user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return {
        "full_name": existing_user.full_name,
        "email": existing_user.email
    }
@app.post("/resume/upload")
def upload_resume(
    file: UploadFile = File(...),
    token: str = Depends(oauth2_scheme)
):
    email = verify_access_token(token)

    db = SessionLocal()

    existing_user = db.query(User).filter(
        User.email == email
    ).first()

    if existing_user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
    )
    file_path = os.path.join(
    UPLOAD_DIR,
    f"{existing_user.id}_{file.filename}"
)
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
        reader = PdfReader(file_path)
        resume_text = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                resume_text += text+"\n"
        new_resume = Resume(
            user_id=existing_user.id,
            filename=file.filename,
            file_path=file_path,
            resume_text=resume_text
        )
        db.add(new_resume)
        db.commit()
        db.refresh(new_resume)

            
    return {
        "message": "Resume uploaded successfully",
        "resume_id": new_resume.id,
        "filename": new_resume.filename,
        "text_length": len(resume_text)
    }

@app.post("/resume/analyze/{resume_id}")
def analyze_resume(
    resume_id: int,
    request: ResumeAnalysisRequest,
    token: str = Depends(oauth2_scheme)
):
    email = verify_access_token(token)

    db = SessionLocal()

    existing_user = db.query(User).filter(
        User.email == email
    ).first()

    if existing_user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    resume = db.query(models.Resume).filter(models.Resume.id == resume_id,
        models.Resume.user_id == existing_user.id
    ).first()

    if resume is None:
        raise HTTPException(
            status_code=404,
            detail="No resume found"
        )
    target_role = request.target_role
    if target_role not in ROLE_SKILLS:
        raise HTTPException(
            status_code=400,
            detail="Invalid target role"
        )
    required_skills = ROLE_SKILLS[target_role]

    resume_text = resume.resume_text.lower()
    found_skills=[]
    for skill in required_skills:
        skill_pattern = r"\b" + re.escape(skill.lower()) + r"\b"
        if re.search(skill_pattern, resume_text):
            found_skills.append(skill)
    missing_skills = []
    for skill in required_skills:
        if skill not in found_skills:
            missing_skills.append(skill)
    recommendations = []
    for skill in missing_skills:
        recommendations.append(f"Consider learning {skill} to improve your chances for the {target_role} role.")

    return {
        "resume_id": resume.id,
        "filename": resume.filename,
        "text_length": len(resume.resume_text),
        "target_role": target_role,
        "required_skills": required_skills,
        "found_skills": found_skills,
        "missing_skills": missing_skills,
        "recommendations": recommendations
    }

    