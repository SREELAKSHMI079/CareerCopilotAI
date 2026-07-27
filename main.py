from fastapi import FastAPI
from database import engine, Base,SessionLocal
import models
from schemas import UserCreate
from schemas import UserLogin

from models import User 
from auth import hash_password
from auth import verify_password

from fastapi import HTTPException


Base.metadata.create_all(bind=engine)
app=FastAPI()


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
def login_user(user:UserLogin):
    db=SessionLocal()
    existing_user=db.query(User).filter(User.email==user.email).first()
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
    return {
        "message":"LOGIN SUCCESSFULL-WELCOME TO CAREERCOPILOT"
    }
    
