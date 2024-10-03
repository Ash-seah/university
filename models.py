from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base
import enum

# Enum for subject choices
class SubjectEnum(enum.Enum):
    RIAZI = "Riazi"
    TAJROBI = "Tajrobi"
    ENSANI = "Ensani"

# User Model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # Relationship with Classes
    classes = relationship("Classes", back_populates="owner")


# Classes Model
class Classes(Base):
    __tablename__ = 'classes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, nullable=True)
    owner_id = Column(Integer, ForeignKey('users.id'))  # ForeignKey to User

    # Enum field for subjects with choices: Riazi, Tajrobi, Ensani
    subject = Column(Enum(SubjectEnum), nullable=False)

    # Relationship back to the user
    owner = relationship("User", back_populates="classes")

    # Relationship with Teachers and Discounts
    teachers = relationship("Teachers", back_populates="class_info")
    discounts = relationship("Discount", back_populates="classes")


# Teachers Model
class Teachers(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    subject = Column(String)
    class_id = Column(Integer, ForeignKey('classes.id'))  # ForeignKey to Classes

    # Relationship back to Classes
    class_info = relationship("Classes", back_populates="teachers")


# Notification Model
class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)  # Timestamp when created
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Timestamp when updated
    slug = Column(String, unique=True, index=True)  # Unique slug for the notification

    # Relationships with News and Discount
    news = relationship("News", back_populates="notification", cascade="all, delete-orphan")
    discounts = relationship("Discount", back_populates="notification", cascade="all, delete-orphan")


# News Model
class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)  # Description of the news
    notification_id = Column(Integer, ForeignKey("notifications.id"))  # Foreign key to Notification

    # Relationship back to Notification
    notification = relationship("Notification", back_populates="news")


# Discount Model
class Discount(Base):
    __tablename__ = "discounts"

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)  # Quantity for the discount
    start_time = Column(DateTime)  # Start time of the discount
    end_time = Column(DateTime)  # End time of the discount
    notification_id = Column(Integer, ForeignKey("notifications.id"))  # Foreign key to Notification
    class_id = Column(Integer, ForeignKey("classes.id"))  # Foreign key to Classes

    # Relationships
    notification = relationship("Notification", back_populates="discounts")
    classes = relationship("Classes", back_populates="discounts")
    courses = relationship("Courses", back_populates="discount")


# Courses Model
class Courses(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String)  # Subject of the course
    description = Column(String)  # Description of the course
    number_of_sessions = Column(Integer)  # Number of sessions in the course
    discount_id = Column(Integer, ForeignKey("discounts.id"))  # Foreign key to Discount

    # Relationship back to Discount
    discount = relationship("Discount", back_populates="courses")
