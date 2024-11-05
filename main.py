from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import Session
from typing import List
from .database import init_db, get_session
from .crud import (
    create_student,
    get_students,
    get_student,
    update_student,
    delete_student,
)
from .models import Student, StudentCreate

app = FastAPI()

# Initialize the database on startup
@app.on_event("startup")
def on_startup():
    init_db()

@app.post("/students/", response_model=Student)
def create_student_endpoint(student: StudentCreate, session: Session = Depends(get_session)):
    return create_student(session, student)

@app.get("/students/", response_model=List[Student])
def read_students_endpoint(session: Session = Depends(get_session)):
    return get_students(session)

@app.get("/students/{student_id}", response_model=Student)
def read_student_endpoint(student_id: int, session: Session = Depends(get_session)):
    student = get_student(session, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put("/students/{student_id}", response_model=Student)
def update_student_endpoint(student_id: int, student: StudentCreate, session: Session = Depends(get_session)):
    updated_student = update_student(session, student_id, student)
    if not updated_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student

@app.delete("/students/{student_id}")
def delete_student_endpoint(student_id: int, session: Session = Depends(get_session)):
    if not delete_student(session, student_id):
        raise HTTPException(status_code=404, detail="Student not found")
    return {"detail": "Student deleted"}
