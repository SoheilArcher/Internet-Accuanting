def test_health_checks_database(client):
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "database": "ok"}


def test_owner_can_list_tenants(client):
    response = client.get("/api/v1/owner/tenants")

    assert response.status_code == 200
    tenants = response.json()
    assert tenants
    assert tenants[0]["name"] == "اپراتور شرق"
    assert tenants[0]["destination_attribution_enabled"] is False


def test_tenant_dashboard_returns_operational_counts(client):
    response = client.get("/api/v1/tenants/1/dashboard")

    assert response.status_code == 200
    data = response.json()
    assert data["users_total"] >= 3
    assert data["users_online"] >= 2
    assert data["invoices_open"] >= 1
    assert data["tickets_open"] >= 1
    assert data["routers_active"] >= 1


def test_isp_manager_can_create_user(client):
    payload = {
        "username": "new-user-100",
        "full_name": "کاربر جدید",
        "mobile": "09120000099",
        "service_name": "PPPoE 50GB",
        "wallet_balance": "1500000",
    }

    response = client.post("/api/v1/tenants/1/users", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["username"] == payload["username"]
    assert data["service_name"] == payload["service_name"]


def test_customer_or_support_can_create_ticket(client):
    payload = {
        "user_id": 1,
        "subject": "مشکل شارژ سرویس",
        "priority": "high",
        "message": "پرداخت انجام شده ولی سرویس تمدید نشده است.",
    }

    response = client.post("/api/v1/tenants/1/tickets", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["subject"] == payload["subject"]
    assert data["status"] == "open"
    assert data["priority"] == "high"


def test_destination_report_is_owner_only(client):
    blocked = client.get("/api/v1/tenants/1/attribution/destinations")
    allowed = client.get(
        "/api/v1/tenants/1/attribution/destinations",
        headers={"X-Platform-Owner": "true"},
    )

    assert blocked.status_code == 403
    assert blocked.json()["detail"] == "Destination attribution is owner-only by default"
    assert allowed.status_code == 200
    assert allowed.json()[0]["username"] == "mohsen-021"

