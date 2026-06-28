from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class TenantRead(BaseModel):
    id: int
    name: str
    status: str
    license_expires_at: date
    destination_attribution_enabled: bool

    model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=80)
    full_name: str = Field(min_length=2, max_length=160)
    mobile: str | None = None
    service_name: str = Field(min_length=2, max_length=120)
    wallet_balance: Decimal = Decimal("0")


class UserRead(BaseModel):
    id: int
    tenant_id: int
    username: str
    full_name: str
    mobile: str | None
    role: str
    status: str
    service_name: str
    wallet_balance: Decimal
    is_online: bool
    assigned_ip: str | None
    nas_name: str | None
    online_since: datetime | None
    download_bytes: int
    upload_bytes: int

    model_config = ConfigDict(from_attributes=True)


class InvoiceRead(BaseModel):
    id: int
    tenant_id: int
    user_id: int | None
    number: str
    item_name: str
    amount: Decimal
    status: str
    issued_at: date

    model_config = ConfigDict(from_attributes=True)


class TicketCreate(BaseModel):
    user_id: int | None = None
    subject: str = Field(min_length=3, max_length=180)
    priority: str = "normal"
    message: str = Field(min_length=2, max_length=4000)


class TicketRead(BaseModel):
    id: int
    tenant_id: int
    user_id: int | None
    subject: str
    status: str
    priority: str
    assigned_to: str | None

    model_config = ConfigDict(from_attributes=True)


class RouterRead(BaseModel):
    id: int
    tenant_id: int
    name: str
    device_type: str
    ip_address: str
    radius_status: str
    accounting_status: str
    status: str

    model_config = ConfigDict(from_attributes=True)


class ResellerRead(BaseModel):
    id: int
    tenant_id: int
    name: str
    credit_balance: Decimal
    sales_month: Decimal
    commission_percent: Decimal
    status: str

    model_config = ConfigDict(from_attributes=True)


class DashboardRead(BaseModel):
    tenant: TenantRead
    users_total: int
    users_online: int
    invoices_open: int
    revenue_paid: Decimal
    tickets_open: int
    routers_active: int


class DestinationRecord(BaseModel):
    username: str
    assigned_ip: str
    destination: str
    destination_port: int
    protocol: str
    nas_name: str
    confidence: str

