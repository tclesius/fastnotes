from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.core import get_db
from note.models import NoteRead, NoteCreate, NoteUpdate
from note.service import get_paginated, get, create, update, delete, search
from user import models
from user.auth import get_authenticated_user

router = APIRouter()


@router.get("", response_model=List[NoteRead])
async def get_notes(skip: int, limit: int, db_session: Session = Depends(get_db),
                    current_user: models.User = Depends(get_authenticated_user)):
    return get_paginated(db_session=db_session, skip=skip, limit=limit, user=current_user)


@router.post("/{query}", response_model=List[NoteRead])
async def search_notes(skip: int, limit: int, title_query: str, db_session: Session = Depends(get_db),
                       current_user: models.User = Depends(get_authenticated_user)):
    return search(db_session=db_session, title=title_query, skip=skip, limit=limit, user=current_user)


@router.get("/{note_id}", response_model=NoteRead)
async def get_note(note_id: int, db_session: Session = Depends(get_db),
                   current_user: models.User = Depends(get_authenticated_user)):
    note = get(db_session=db_session, note_id=note_id, user=current_user)
    if not note:
        raise HTTPException(status_code=404, detail=[{"message": "Note not found."}])
    return note


@router.post("", response_model=NoteRead)
async def create_note(note_in: NoteCreate, db_session: Session = Depends(get_db),
                      current_user: models.User = Depends(get_authenticated_user)):
    note = create(db_session=db_session, note_in=note_in, user=current_user)
    return note


@router.patch("/{note_id}")
async def update_note(note_id: int, note_in: NoteUpdate, db_session: Session = Depends(get_db),
                      current_user: models.User = Depends(get_authenticated_user)):
    update(db_session=db_session, note_id=note_id, note_in=note_in, user=current_user)


@router.delete("/{note_id}")
async def delete_note(note_id: int, db_session: Session = Depends(get_db),
                      current_user: models.User = Depends(get_authenticated_user)):
    delete(db_session=db_session, note_id=note_id, user=current_user)
