from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.event import Event, EventCreate
from app.services.event_service import EventService

router = APIRouter()

@router.get("/", response_model=List[Event])
def read_events(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
):
    events = EventService.get_multi(db, skip=skip, limit=limit)
    return events

@router.post("/", response_model=Event)
def create_event(
    *,
    db: Session = Depends(deps.get_db),
    event_in: EventCreate,
):
    event = EventService.create(db, obj_in=event_in)
    return event

@router.get("/{event_id}", response_model=Event)
def read_event(
    *,
    db: Session = Depends(deps.get_db),
    event_id: int,
):
    event = EventService.get(db, id=event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event
