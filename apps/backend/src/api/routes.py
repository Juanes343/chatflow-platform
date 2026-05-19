from fastapi import APIRouter

router = APIRouter()


@router.get("/tenants")
def list_tenants() -> list[dict[str, str]]:
    return [{"id": "demo-tenant", "name": "Demo Tenant"}]


@router.post("/webhooks/whatsapp")
def whatsapp_webhook(payload: dict) -> dict[str, str]:
    # TODO: verify signature and enqueue async processing
    return {"received": "true"}


@router.post("/messages/send")
def send_message(payload: dict) -> dict[str, str]:
    # TODO: push outbound queue -> WhatsApp Cloud API
    return {"status": "queued"}
