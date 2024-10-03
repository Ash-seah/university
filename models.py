from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

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

    # Relationship back to the user
    owner = relationship("User", back_populates="classes")

    # Relationships with Riazi, Tajrobi, Ensani, and Teachers
    riazi = relationship("Riazi", back_populates="class_info")
    tajrobi = relationship("Tajrobi", back_populates="class_info")
    ensani = relationship("Ensani", back_populates="class_info")
    teachers = relationship("Teachers", back_populates="class_info")


# Riazi Model
class Riazi(Base):
    __tablename__ = 'riazi'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    class_id = Column(Integer, ForeignKey('classes.id'))  # ForeignKey to Classes

    # Relationship back to Classes
    class_info = relationship("Classes", back_populates="riazi")


# Tajrobi Model
class Tajrobi(Base):
    __tablename__ = 'tajrobi'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    class_id = Column(Integer, ForeignKey('classes.id'))  # ForeignKey to Classes

    # Relationship back to Classes
    class_info = relationship("Classes", back_populates="tajrobi")


# Ensani Model
class Ensani(Base):
    __tablename__ = 'ensani'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    class_id = Column(Integer, ForeignKey('classes.id'))  # ForeignKey to Classes

    # Relationship back to Classes
    class_info = relationship("Classes", back_populates="ensani")


# Teachers Model
class Teachers(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    subject = Column(String)
    class_id = Column(Integer, ForeignKey('classes.id'))  # ForeignKey to Classes

    # Relationship back to Classes
    class_info = relationship("Classes", back_populates="teachers")
