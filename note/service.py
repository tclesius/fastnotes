import sqlalchemy
from sqlalchemy.orm import Session

from note.models import Note, NoteCreate, NoteUpdate
from user.models import User


def get(*, db_session: Session, note_id: int, user: User):
    stmt = sqlalchemy.select(Note).filter(Note.id == note_id, Note.user_id == user.id)
    return db_session.execute(stmt).scalars().first()


def get_paginated(*, db_session: Session, skip: int, limit: int, user: User):
    stmt = sqlalchemy.select(Note).filter(Note.user_id == user.id).offset(skip).limit(limit)
    return db_session.execute(stmt).scalars().all()


def create(*, db_session: Session, note_in: NoteCreate, user: User):
    note = Note(**note_in.dict(), user_id=user.id)
    db_session.add(note)
    db_session.commit()
    db_session.refresh(note)
    return note


def update(*, db_session: Session, note_id: int, note_in: NoteUpdate, user: User):
    stmt = sqlalchemy.update(Note) \
        .where(Note.id == note_id, Note.user_id == user.id) \
        .values(**note_in.dict())
    result = db_session.execute(stmt)
    db_session.commit()
    return result.rowcount


def delete(*, db_session: Session, note_id: int, user: User):
    stmt = sqlalchemy.delete(Note).where(Note.id == note_id, Note.user_id == user.id)
    result = db_session.execute(stmt)
    db_session.commit()
    return result.rowcount


def search(*, db_session: Session, title: str, skip: int, limit: int, user: User):
    stmt = sqlalchemy.select(Note).filter(
        Note.title.contains(title, autoescape=True), Note.user_id == user.id
    ).offset(skip).limit(limit)
    return db_session.execute(stmt).scalars().all()
