from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class EventBase(BaseModel):
    title: str
    description: Optional[str] = None
    date: datetime
    location: Optional[str] = None
    price: float
    tickets_available: int

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int
    organizer_id: int

    class Config:
        orm_mode = True
