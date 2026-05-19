# Chatflow Platform MVP

Monorepo MVP SaaS IA para WhatsApp con FastAPI + Next.js + Celery + Redis + PostgreSQL.

## Apps
- `apps/backend`: API principal + webhooks + websocket.
- `apps/worker`: workers async.
- `apps/frontend`: dashboard Next.js.

## Quick start
```bash
docker compose -f infra/compose/docker-compose.dev.yml up --build
```
