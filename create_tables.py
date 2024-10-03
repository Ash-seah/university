# create_tables.py
from database import Base, engine
from models import User, Classes, Riazi, Tajrobi, Ensani, Teachers

# This will create all the tables defined in models.py
Base.metadata.create_all(bind=engine)

print("Tables created successfully.")
