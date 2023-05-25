from pydantic import BaseModel, Field, validator
from sqlalchemy import Column, Integer, String, Text

from database.core import Base


# SQLAlchemy models
class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    text = Column(Text)


# Pydantic models
class NoteBase(BaseModel):
    title: str
    text: str | None = None

    @validator('*', pre=True)
    def empty_str_to_none(cls, v):
        if v == '':
            return None
        return v

    class Config:
        orm_mode = True


class NoteRead(NoteBase):
    id: int


class NoteCreate(NoteBase):
    pass


class NoteUpdate(NoteBase):
    title: str | None
    text: str | None
