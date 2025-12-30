from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.order import Order, OrderCreate
from app.services.order_service import OrderService

router = APIRouter()

@router.post("/", response_model=Order)
def create_order(
    *,
    db: Session = Depends(deps.get_db),
    order_in: OrderCreate,
):
    order = OrderService.create(db, obj_in=order_in)
    return order
