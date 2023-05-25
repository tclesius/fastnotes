import sqlalchemy
from sqlalchemy.orm import Session

from note.models import Note, NoteCreate, NoteUpdate


def get(*, db_session: Session, note_id: int):
    stmt = sqlalchemy.select(Note).filter(Note.id == note_id)
    return db_session.execute(stmt).scalars().first()


def get_paginated(*, db_session: Session, skip: int, limit: int):
    stmt = sqlalchemy.select(Note).offset(skip).limit(limit)
    return db_session.execute(stmt).scalars().all()


def create(*, db_session: Session, note_in: NoteCreate):
    stmt = sqlalchemy.insert(Note).values(**note_in.dict()).returning(Note)
    note = db_session.execute(stmt)
    db_session.commit()
    return note.scalar()


def update(*, db_session: Session, note_id: int, note_in: NoteUpdate):
    stmt = sqlalchemy.update(Note).values(**note_in.dict(exclude_none=True)) \
        .where(Note.id == note_id) \
        .returning(Note)
    note = db_session.execute(stmt)
    db_session.commit()
    return note.scalar()


def delete(*, db_session: Session, note_id: int):
    stmt = sqlalchemy.delete(Note).filter(Note.id == note_id)
    db_session.execute(stmt)
    db_session.commit()


def search(*, db_session: Session, title: str, skip: int, limit: int):
    stmt = sqlalchemy.select(Note).filter(Note.title.contains(title, autoescape=True)).offset(skip).limit(limit)
    return db_session.execute(stmt).scalars().all()

