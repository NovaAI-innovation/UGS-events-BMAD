from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
import datetime

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String)
    date = Column(DateTime, nullable=False)
    location = Column(String)
    price = Column(Float, nullable=False)
    tickets_available = Column(Integer, default=0)
    organizer_id = Column(Integer, ForeignKey("users.id"))
    
    organizer = relationship("User", backref="events")
