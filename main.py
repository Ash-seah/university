from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal
from models import User, Classes, Riazi, Tajrobi, Ensani
from auth import get_password_hash, verify_password, create_access_token  # Optional if you want to add authentication
from typing import List

app = FastAPI()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Pydantic schemas for input validation
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class ClassCreate(BaseModel):
    name: str
    description: str

class RiaziCreate(BaseModel):
    name: str
    description: str
    class_id: int  # References the Classes model

class TajrobiCreate(BaseModel):
    name: str
    description: str
    class_id: int

class EnsaniCreate(BaseModel):
    name: str
    description: str
    class_id: int


# Create a user (this endpoint can be extended with authentication later)
@app.post("/users/")
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(user_data.password)  # Password hashing (optional)
    new_user = User(username=user_data.username, email=user_data.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# Create a class
@app.post("/classes/")
def create_class(class_data: ClassCreate, db: Session = Depends(get_db)):
    new_class = Classes(name=class_data.name, description=class_data.description)
    db.add(new_class)
    db.commit()
    db.refresh(new_class)
    return new_class


# Create Riazi associated with a class
@app.post("/riazi/")
def create_riazi(riazi_data: RiaziCreate, db: Session = Depends(get_db)):
    db_class = db.query(Classes).filter(Classes.id == riazi_data.class_id).first()
    if db_class is None:
        raise HTTPException(status_code=404, detail="Class not found")

    new_riazi = Riazi(name=riazi_data.name, description=riazi_data.description, class_id=riazi_data.class_id)
    db.add(new_riazi)
    db.commit()
    db.refresh(new_riazi)
    return new_riazi


# Create Tajrobi associated with a class
@app.post("/tajrobi/")
def create_tajrobi(tajrobi_data: TajrobiCreate, db: Session = Depends(get_db)):
    db_class = db.query(Classes).filter(Classes.id == tajrobi_data.class_id).first()
    if db_class is None:
        raise HTTPException(status_code=404, detail="Class not found")

    new_tajrobi = Tajrobi(name=tajrobi_data.name, description=tajrobi_data.description, class_id=tajrobi_data.class_id)
    db.add(new_tajrobi)
    db.commit()
    db.refresh(new_tajrobi)
    return new_tajrobi


# Create Ensani associated with a class
@app.post("/ensani/")
def create_ensani(ensani_data: EnsaniCreate, db: Session = Depends(get_db)):
    db_class = db.query(Classes).filter(Classes.id == ensani_data.class_id).first()
    if db_class is None:
        raise HTTPException(status_code=404, detail="Class not found")

    new_ensani = Ensani(name=ensani_data.name, description=ensani_data.description, class_id=ensani_data.class_id)
    db.add(new_ensani)
    db.commit()
    db.refresh(new_ensani)
    return new_ensani


# Retrieve all classes
@app.get("/classes/", response_model=List[ClassCreate])
def get_classes(db: Session = Depends(get_db)):
    return db.query(Classes).all()


# Retrieve all Riazi entries
@app.get("/riazi/", response_model=List[RiaziCreate])
def get_riazi(db: Session = Depends(get_db)):
    return db.query(Riazi).all()


# Retrieve all Tajrobi entries
@app.get("/tajrobi/", response_model=List[TajrobiCreate])
def get_tajrobi(db: Session = Depends(get_db)):
    return db.query(Tajrobi).all()


# Retrieve all Ensani entries
@app.get("/ensani/", response_model=List[EnsaniCreate])
def get_ensani(db: Session = Depends(get_db)):
    return db.query(Ensani).all()
