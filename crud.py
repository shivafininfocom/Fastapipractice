from sqlmodel import Session, select
from typing import List, Optional
from .models import Student, StudentCreate

def create_student(session: Session, student: StudentCreate) -> Student:
    db_student = Student.from_orm(student)
    session.add(db_student)
    session.commit()
    session.refresh(db_student)
    return db_student

def get_students(session: Session) -> List[Student]:
    students = session.exec(select(Student)).all()
    return students

def get_student(session: Session, student_id: int) -> Optional[Student]:
    student = session.get(Student, student_id)
    return student

def update_student(session: Session, student_id: int, student_data: StudentCreate) -> Optional[Student]:
    student = session.get(Student, student_id)
    if student:
        for key, value in student_data.dict().items():
            setattr(student, key, value)
        session.commit()
        session.refresh(student)
        return student
    return None

def delete_student(session: Session, student_id: int) -> bool:
    student = session.get(Student, student_id)
    if student:
        session.delete(student)
        session.commit()
        return True
    return False


