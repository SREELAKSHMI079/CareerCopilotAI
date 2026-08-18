from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from database import engine, Base, SessionLocal
import models
from schemas import UserCreate
from schemas import UserLogin
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from models import User 
from auth import (hash_password,verify_password,create_access_token,verify_access_token)

Base.metadata.create_all(bind=engine)
app=FastAPI()
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