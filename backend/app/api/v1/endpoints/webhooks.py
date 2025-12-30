from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/stripe")
async def stripe_webhook(request: Request):
    # ... handle stripe webhook
    return {"status": "success"}
