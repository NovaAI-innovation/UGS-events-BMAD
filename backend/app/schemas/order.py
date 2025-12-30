from typing import List
from pydantic import BaseModel
from datetime import datetime

class OrderBase(BaseModel):
    pass

class OrderCreate(OrderBase):
    event_id: int
    quantity: int

class Order(OrderBase):
    id: int
    user_id: int
    total_amount: float
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
