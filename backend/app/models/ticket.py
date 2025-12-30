from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"))
    order_id = Column(Integer, ForeignKey("orders.id"))
    qr_code = Column(String, unique=True, index=True)
    status = Column(String, default="valid")

    event = relationship("Event")
    order = relationship("Order")
