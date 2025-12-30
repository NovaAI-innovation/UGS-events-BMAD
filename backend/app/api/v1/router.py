from fastapi import APIRouter
from app.api.v1.endpoints import auth, events, orders, webhooks

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(events.router, prefix="/events", tags=["events"])
api_router.include_router(orders.router, prefix="/orders", tags=["orders"])
api_router.include_router(webhooks.router, prefix="/webhooks", tags=["webhooks"])
