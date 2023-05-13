from typing import List

from fastapi import APIRouter, Depends, HTTPException

from database.core import get_db
from note.models import NoteRead, NoteCreate, NoteUpdate
from note.service import get_paginated, get, create, update, delete

router = APIRouter()


@router.get("", response_model=List[NoteRead])
async def get_notes(skip: int, limit: int, db_session=Depends(get_db)):
    return get_paginated(db_session=db_session, skip=skip, limit=limit)


@router.get("/{note_id}", response_model=NoteRead)
async def get_note(note_id: int, db_session=Depends(get_db)):
    note = get(db_session=db_session, note_id=note_id)
    if not note:
        raise HTTPException(status_code=404,
                            detail=[{"message": "Note not found."}])
    return note


@router.post("", response_model=NoteRead)
async def create_note(note_in: NoteCreate, db_session=Depends(get_db)):
    note = create(db_session=db_session, note_in=note_in)
    return note

@router.patch("/{note_id}", response_model=NoteRead)
async def update_note(note_id: int, note_in: NoteUpdate, db_session=Depends(get_db)):
    note = update(db_session=db_session, note_id=note_id, note_in=note_in)
    return note

@router.delete("/{note_id}")
async def delete_note(note_id: int, db_session=Depends(get_db)):
    delete(db_session=db_session, note_id=note_id)