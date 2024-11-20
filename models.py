from sqlmodel import SQLModel, Field
from typing import Optional

class Student(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int
    grade: str

# Pydantic model for creating a student
class StudentCreate(SQLModel):
    name: str
    age: int
    grade: str


class NewModelGit(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: Optional[int]
    grade: Optional[str]