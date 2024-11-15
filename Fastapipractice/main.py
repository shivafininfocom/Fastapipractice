# app/main.py
from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from database import init_db, get_session
from models import ExampleModel

app = FastAPI()

# Initialize the database when the app starts
@app.on_event("startup")
def on_startup():
    init_db()

# Endpoint to create an example entry
@app.post("/examples/", response_model=ExampleModel)
def create_example(example: ExampleModel, session: Session = Depends(get_session)):
    session.add(example)
    session.commit()
    session.refresh(example)
    return example

# Endpoint to read all examples
@app.get("/examples/", response_model=list[ExampleModel])
def read_examples(session: Session = Depends(get_session)):
    examples = session.exec(select(ExampleModel)).all()
    return examples


