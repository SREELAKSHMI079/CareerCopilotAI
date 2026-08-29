from sqlalchemy import Column, Integer, String,DateTime,ForeignKey,Text
from sqlalchemy.orm import relationship

from database import Base
from datetime import datetime
class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    full_name=Column(String,nullable=False)
    email=Column(String,unique=True,nullable=False)
    password_hash=Column(String,nullable=False)
    created_at=Column(DateTime,default=datetime.utcnow)
    resumes = relationship("Resume", back_populates="user")
class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    filename = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    resume_text = Column(Text, nullable=True)
    uploaded_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship("User", back_populates="resumes")
