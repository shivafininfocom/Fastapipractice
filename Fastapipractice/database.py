# app/database.py
from sqlmodel import SQLModel, Session, create_engine
from config import DATABASE_URL  # Import the database URL directly

# Create the database engine with the hardcoded DATABASE_URL
engine = create_engine(DATABASE_URL, echo=True)

# Function to initialize the database
def init_db():
    SQLModel.metadata.create_all(engine)

# Dependency to get a session for each request
def get_session():
    with Session(engine) as session:
        yield session
