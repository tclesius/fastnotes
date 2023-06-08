from pydantic import BaseModel, Field, validator
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from database.core import Base


# SQLAlchemy models
class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    text = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="notes")


# Pydantic models
class NoteBase(BaseModel):
    title: str
    text: str | None = None

    class Config:
        orm_mode = True


class NoteRead(NoteBase):
    id: int


class NoteCreate(NoteBase):
    pass


class NoteUpdate(NoteBase):
    title: str | None
    text: str | None
