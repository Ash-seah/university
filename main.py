from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal
from models import User, Classes,  Teachers, Notification, News, Discount, Courses
from typing import List
from auth import get_password_hash, verify_password, create_access_token, get_current_user
from datetime import datetime

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------------ Pydantic Schemas ------------------------
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class ClassCreate(BaseModel):
    name: str
    description: str

class ClassUpdate(BaseModel):
    name: str
    description: str

class NotificationCreate(BaseModel):
    slug: str

class NotificationUpdate(BaseModel):
    slug: str

class NewsCreate(BaseModel):
    description: str
    notification_id: int

class NewsUpdate(BaseModel):
    description: str

class DiscountCreate(BaseModel):
    quantity: int
    start_time: datetime
    end_time: datetime
    notification_id: int
    class_id: int

class DiscountUpdate(BaseModel):
    quantity: int
    start_time: datetime
    end_time: datetime

class CourseCreate(BaseModel):
    subject: str
    description: str
    number_of_sessions: int
    discount_id: int

class CourseUpdate(BaseModel):
    subject: str
    description: str
    number_of_sessions: int

# ------------------------ CRUD Endpoints for Notifications ------------------------

# Create notification
@app.post("/notifications/", response_model=NotificationCreate)
def create_notification(notification_data: NotificationCreate, db: Session = Depends(get_db)):
    new_notification = Notification(slug=notification_data.slug)
    db.add(new_notification)
    db.commit()
    db.refresh(new_notification)
    return new_notification

# Update notification
@app.put("/notifications/{notification_id}/", response_model=NotificationUpdate)
def update_notification(notification_id: int, notification_data: NotificationUpdate, db: Session = Depends(get_db)):
    notification = db.query(Notification).filter(Notification.id == notification_id).first()
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    
    notification.slug = notification_data.slug
    db.commit()
    db.refresh(notification)
    return notification

# Delete notification
@app.delete("/notifications/{notification_id}/")
def delete_notification(notification_id: int, db: Session = Depends(get_db)):
    notification = db.query(Notification).filter(Notification.id == notification_id).first()
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    
    db.delete(notification)
    db.commit()
    return {"message": "Notification deleted successfully"}

# Retrieve all notifications
@app.get("/notifications/", response_model=List[NotificationCreate])
def get_notifications(db: Session = Depends(get_db)):
    return db.query(Notification).all()

# ------------------------ CRUD Endpoints for News ------------------------

# Create news
@app.post("/news/", response_model=NewsCreate)
def create_news(news_data: NewsCreate, db: Session = Depends(get_db)):
    notification = db.query(Notification).filter(Notification.id == news_data.notification_id).first()
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    
    new_news = News(description=news_data.description, notification_id=news_data.notification_id)
    db.add(new_news)
    db.commit()
    db.refresh(new_news)
    return new_news

# Update news
@app.put("/news/{news_id}/", response_model=NewsUpdate)
def update_news(news_id: int, news_data: NewsUpdate, db: Session = Depends(get_db)):
    news = db.query(News).filter(News.id == news_id).first()
    if not news:
        raise HTTPException(status_code=404, detail="News not found")
    
    news.description = news_data.description
    db.commit()
    db.refresh(news)
    return news

# Delete news
@app.delete("/news/{news_id}/")
def delete_news(news_id: int, db: Session = Depends(get_db)):
    news = db.query(News).filter(News.id == news_id).first()
    if not news:
        raise HTTPException(status_code=404, detail="News not found")
    
    db.delete(news)
    db.commit()
    return {"message": "News deleted successfully"}

# Retrieve all news
@app.get("/news/", response_model=List[NewsCreate])
def get_news(db: Session = Depends(get_db)):
    return db.query(News).all()

# ------------------------ CRUD Endpoints for Discounts ------------------------

# Create discount
@app.post("/discounts/", response_model=DiscountCreate)
def create_discount(discount_data: DiscountCreate, db: Session = Depends(get_db)):
    notification = db.query(Notification).filter(Notification.id == discount_data.notification_id).first()
    db_class = db.query(Classes).filter(Classes.id == discount_data.class_id).first()
    if not notification or not db_class:
        raise HTTPException(status_code=404, detail="Notification or Class not found")
    
    new_discount = Discount(
        quantity=discount_data.quantity,
        start_time=discount_data.start_time,
        end_time=discount_data.end_time,
        notification_id=discount_data.notification_id,
        class_id=discount_data.class_id
    )
    db.add(new_discount)
    db.commit()
    db.refresh(new_discount)
    return new_discount

# Update discount
@app.put("/discounts/{discount_id}/", response_model=DiscountUpdate)
def update_discount(discount_id: int, discount_data: DiscountUpdate, db: Session = Depends(get_db)):
    discount = db.query(Discount).filter(Discount.id == discount_id).first()
    if not discount:
        raise HTTPException(status_code=404, detail="Discount not found")
    
    discount.quantity = discount_data.quantity
    discount.start_time = discount_data.start_time
    discount.end_time = discount_data.end_time
    db.commit()
    db.refresh(discount)
    return discount

# Delete discount
@app.delete("/discounts/{discount_id}/")
def delete_discount(discount_id: int, db: Session = Depends(get_db)):
    discount = db.query(Discount).filter(Discount.id == discount_id).first()
    if not discount:
        raise HTTPException(status_code=404, detail="Discount not found")
    
    db.delete(discount)
    db.commit()
    return {"message": "Discount deleted successfully"}

# Retrieve all discounts
@app.get("/discounts/", response_model=List[DiscountCreate])
def get_discounts(db: Session = Depends(get_db)):
    return db.query(Discount).all()

# ------------------------ CRUD Endpoints for Classes ------------------------

# Create a class
@app.post("/classes/", response_model=ClassCreate)
def create_class(class_data: ClassCreate, db: Session = Depends(get_db)):
    new_class = Classes(name=class_data.name, description=class_data.description)
    db.add(new_class)
    db.commit()
    db.refresh(new_class)
    return new_class

# Update class
@app.put("/classes/{class_id}/", response_model=ClassUpdate)
def update_class(class_id: int, class_data: ClassUpdate, db: Session = Depends(get_db)):
    db_class = db.query(Classes).filter(Classes.id == class_id).first()
    if not db_class:
        raise HTTPException(status_code=404, detail="Class not found")

    db_class.name = class_data.name
    db_class.description = class_data.description
    db.commit()
    db.refresh(db_class)
    return db_class

# Delete class
@app.delete("/classes/{class_id}/")
def delete_class(class_id: int, db: Session = Depends(get_db)):
    db_class = db.query(Classes).filter(Classes.id == class_id).first()
    if not db_class:
        raise HTTPException(status_code=404, detail="Class not found")
    
    db.delete(db_class)
    db.commit()
    return {"message": "Class deleted successfully"}

# Retrieve all classes
@app.get("/classes/", response_model=List[ClassCreate])
def get_classes(db: Session = Depends(get_db)):
    return db.query(Classes).all()

# ------------------------ CRUD Endpoints for Courses ------------------------

# Create course
@app.post("/courses/", response_model=CourseCreate)
def create_course(course_data: CourseCreate, db: Session = Depends(get_db)):
    discount = db.query(Discount).filter(Discount.id == course_data.discount_id).first()
    if not discount:
        raise HTTPException(status_code=404, detail="Discount not found")
    
    new_course = Courses(
        subject=course_data.subject,
        description=course_data.description,
        number_of_sessions=course_data.number_of_sessions,
        discount_id=course_data.discount_id
    )
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course

# Update course
@app.put("/courses/{course_id}/", response_model=CourseUpdate)
def update_course(course_id: int, course_data: CourseUpdate, db: Session = Depends(get_db)):
    course = db.query(Courses).filter(Courses.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    course.subject = course_data.subject
    course.description = course
