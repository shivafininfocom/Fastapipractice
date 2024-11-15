# app/models.py
from sqlmodel import SQLModel, Field
from typing import Optional

class GenData(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=50)
    value: Optional[float] = None
    address: str = Field(max_length=200)

class Electronics(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    itemname: str = Field(max_length=100)

class Locations(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    location_data: str = Field(max_length=100)

