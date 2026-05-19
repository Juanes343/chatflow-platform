from celery import Celery

celery_app = Celery(
    "chatflow_worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/1",
)


@celery_app.task
def process_incoming_message(event_id: str) -> dict[str, str]:
    # TODO: hydrate context, run AI, send outbound message
    return {"event_id": event_id, "status": "processed"}
