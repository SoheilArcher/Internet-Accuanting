# API Service

FastAPI backend for the accounting platform.

## Local Development

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m uvicorn app.main:app --reload --port 8010
```

## Test

```powershell
.venv\Scripts\python.exe -m pytest -q
```

## Current Operational Slice

- `GET /api/v1/health`
- `GET /api/v1/owner/tenants`
- `GET /api/v1/tenants/{tenant_id}/dashboard`
- `GET /api/v1/tenants/{tenant_id}/users`
- `POST /api/v1/tenants/{tenant_id}/users`
- `GET /api/v1/tenants/{tenant_id}/online-users`
- `GET /api/v1/tenants/{tenant_id}/invoices`
- `GET /api/v1/tenants/{tenant_id}/tickets`
- `POST /api/v1/tenants/{tenant_id}/tickets`
- `GET /api/v1/tenants/{tenant_id}/routers`
- `GET /api/v1/tenants/{tenant_id}/resellers`
- `GET /api/v1/tenants/{tenant_id}/attribution/destinations`

Destination attribution is owner-only by default. For the first operational guard, the endpoint requires:

```text
X-Platform-Owner: true
```
