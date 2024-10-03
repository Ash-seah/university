from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from database import SessionLocal
from models import User, Classes, Courses, Notification, News, Discount, Teachers
from auth import get_password_hash, verify_password, create_access_token, get_current_user
from typing import List, Optional
from sqlalchemy.exc import IntegrityError

app = FastAPI()


# Dependency to get the database session
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


class UserLogin(BaseModel):
    username: str
    password: str


class ClassCreate(BaseModel):
    name: str
    description: str
    subject: str = Field(..., pattern="^(Riazi|Tajrobi|Ensani)$")  # Changed regex to pattern


class ClassUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    subject: Optional[str] = Field(None, pattern="^(Riazi|Tajrobi|Ensani)$")  # Changed regex to pattern


class CoursesCreate(BaseModel):
    subject: str
    description: str
    number_of_sessions: int
    discount_id: int


class CoursesUpdate(BaseModel):
    subject: Optional[str]
    description: Optional[str]
    number_of_sessions: Optional[int]
    discount_id: Optional[int]


class NotificationCreate(BaseModel):
    slug: str


class NotificationUpdate(BaseModel):
    slug: Optional[str]


class NewsCreate(BaseModel):
    description: str
    notification_id: int


class NewsUpdate(BaseModel):
    description: Optional[str]


class DiscountCreate(BaseModel):
    quantity: int
    start_time: str
    end_time: str
    notification_id: int
    class_id: int


class DiscountUpdate(BaseModel):
    quantity: Optional[int]
    start_time: Optional[str]
    end_time: Optional[str]
    notification_id: Optional[int]
    class_id: Optional[int]


# Registration endpoint (creates a new user)
@app.post("/register/")
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(user_data.password)
    new_user = User(username=user_data.username, email=user_data.email, hashed_password=hashed_password)
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="User with this username or email already exists.")
    return {"message": "User registered successfully."}


# Login endpoint
@app.post("/login/")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == user_data.username).first()
    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


# Logout endpoint (currently a placeholder)
@app.post("/logout/")
def logout():
    return {"message": "Logout successful. Token would be invalidated in a real application."}


# CRUD for Classes
@app.post("/classes/", response_model=ClassCreate)
def create_class(class_data: ClassCreate, db: Session = Depends(get_db)):
    new_class = Classes(name=class_data.name, description=class_data.description, subject=class_data.subject)
    db.add(new_class)
    db.commit()
    db.refresh(new_class)
    return new_class


@app.get("/classes/", response_model=List[ClassCreate])
def get_classes(db: Session = Depends(get_db)):
    return db.query(Classes).all()


@app.put("/classes/{class_id}", response_model=ClassCreate)
def update_class(class_id: int, class_data: ClassUpdate, db: Session = Depends(get_db)):
    class_instance = db.query(Classes).filter(Classes.id == class_id).first()
    if not class_instance:
        raise HTTPException(status_code=404, detail="Class not found")

    if class_data.name:
        class_instance.name = class_data.name
    if class_data.description:
        class_instance.description = class_data.description
    if class_data.subject:
        class_instance.subject = class_data.subject

    db.commit()
    db.refresh(class_instance)
    return class_instance


@app.delete("/classes/{class_id}")
def delete_class(class_id: int, db: Session = Depends(get_db)):
    class_instance = db.query(Classes).filter(Classes.id == class_id).first()
    if not class_instance:
        raise HTTPException(status_code=404, detail="Class not found")
    db.delete(class_instance)
    db.commit()
    return {"message": "Class deleted successfully."}


# CRUD for Courses
@app.post("/courses/", response_model=CoursesCreate)
def create_course(course_data: CoursesCreate, db: Session = Depends(get_db)):
    new_course = Courses(subject=course_data.subject, description=course_data.description,
                         number_of_sessions=course_data.number_of_sessions, discount_id=course_data.discount_id)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course


@app.get("/courses/", response_model=List[CoursesCreate])
def get_courses(db: Session = Depends(get_db)):
    return db.query(Courses).all()


@app.put("/courses/{course_id}", response_model=CoursesCreate)
def update_course(course_id: int, course_data: CoursesUpdate, db: Session = Depends(get_db)):
    course_instance = db.query(Courses).filter(Courses.id == course_id).first()
    if not course_instance:
        raise HTTPException(status_code=404, detail="Course not found")

    if course_data.subject:
        course_instance.subject = course_data.subject
    if course_data.description:
        course_instance.description = course_data.description
    if course_data.number_of_sessions:
        course_instance.number_of_sessions = course_data.number_of_sessions
    if course_data.discount_id:
        course_instance.discount_id = course_data.discount_id

    db.commit()
    db.refresh(course_instance)
    return course_instance


@app.delete("/courses/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    course_instance = db.query(Courses).filter(Courses.id == course_id).first()
    if not course_instance:
        raise HTTPException(status_code=404, detail="Course not found")
    db.delete(course_instance)
    db.commit()
    return {"message": "Course deleted successfully."}


# CRUD for Notifications
@app.post("/notifications/", response_model=NotificationCreate)
def create_notification(notification_data: NotificationCreate, db: Session = Depends(get_db)):
    new_notification = Notification(slug=notification_data.slug)
    db.add(new_notification)
    db.commit()
    db.refresh(new_notification)
    return new_notification


@app.get("/notifications/", response_model=List[NotificationCreate])
def get_notifications(db: Session = Depends(get_db)):
    return db.query(Notification).all()


@app.put("/notifications/{notification_id}", response_model=NotificationCreate)
def update_notification(notification_id: int, notification_data: NotificationUpdate, db: Session = Depends(get_db)):
    notification_instance = db.query(Notification).filter(Notification.id == notification_id).first()
    if not notification_instance:
        raise HTTPException(status_code=404, detail="Notification not found")

    if notification_data.slug:
        notification_instance.slug = notification_data.slug

    db.commit()
    db.refresh(notification_instance)
    return notification_instance


@app.delete("/notifications/{notification_id}")
def delete_notification(notification_id: int, db: Session = Depends(get_db)):
    notification_instance = db.query(Notification).filter(Notification.id == notification_id).first()
    if not notification_instance:
        raise HTTPException(status_code=404, detail="Notification not found")
    db.delete(notification_instance)
    db.commit()
    return {"message": "Notification deleted successfully."}


# CRUD for News
@app.post("/news/", response_model=NewsCreate)
def create_news(news_data: NewsCreate, db: Session = Depends(get_db)):
    new_news = News(description=news_data.description, notification_id=news_data.notification_id)
    db.add(new_news)
    db.commit()
    db.refresh(new_news)
    return new_news


@app.get("/news/", response_model=List[NewsCreate])
def get_news(db: Session = Depends(get_db)):
    return db.query(News).all()


@app.put("/news/{news_id}", response_model=NewsCreate)
def update_news(news_id: int, news_data: NewsUpdate, db: Session = Depends(get_db)):
    news_instance = db.query(News).filter(News.id == news_id).first()
    if not news_instance:
        raise HTTPException(status_code=404, detail="News not found")

    if news_data.description:
        news_instance.description = news_data.description

    db.commit()
    db.refresh(news_instance)
    return news_instance


@app.delete("/news/{news_id}")
def delete_news(news_id: int, db: Session = Depends(get_db)):
    news_instance = db.query(News).filter(News.id == news_id).first()
    if not news_instance:
        raise HTTPException(status_code=404, detail="News not found")
    db.delete(news_instance)
    db.commit()
    return {"message": "News deleted successfully."}


# CRUD for Discounts
@app.post("/discounts/", response_model=DiscountCreate)
def create_discount(discount_data: DiscountCreate, db: Session = Depends(get_db)):
    new_discount = Discount(quantity=discount_data.quantity, start_time=discount_data.start_time,
                            end_time=discount_data.end_time, notification_id=discount_data.notification_id,
                            class_id=discount_data.class_id)
    db.add(new_discount)
    db.commit()
    db.refresh(new_discount)
    return new_discount


@app.get("/discounts/", response_model=List[DiscountCreate])
def get_discounts(db: Session = Depends(get_db)):
    return db.query(Discount).all()


@app.put("/discounts/{discount_id}", response_model=DiscountCreate)
def update_discount(discount_id: int, discount_data: DiscountUpdate, db: Session = Depends(get_db)):
    discount_instance = db.query(Discount).filter(Discount.id == discount_id).first()
    if not discount_instance:
        raise HTTPException(status_code=404, detail="Discount not found")

    if discount_data.quantity:
        discount_instance.quantity = discount_data.quantity
    if discount_data.start_time:
        discount_instance.start_time = discount_data.start_time
    if discount_data.end_time:
        discount_instance.end_time = discount_data.end_time
    if discount_data.notification_id:
        discount_instance.notification_id = discount_data.notification_id
    if discount_data.class_id:
        discount_instance.class_id = discount_data.class_id

    db.commit()
    db.refresh(discount_instance)
    return discount_instance


@app.delete("/discounts/{discount_id}")
def delete_discount(discount_id: int, db: Session = Depends(get_db)):
    discount_instance = db.query(Discount).filter(Discount.id == discount_id).first()
    if not discount_instance:
        raise HTTPException(status_code=404, detail="Discount not found")
    db.delete(discount_instance)
    db.commit()
    return {"message": "Discount deleted successfully."}