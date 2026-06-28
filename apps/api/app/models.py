from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import Boolean, Date, DateTime, ForeignKey, Integer, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )


class Tenant(TimestampMixin, Base):
    __tablename__ = "tenants"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(160), unique=True, index=True)
    status: Mapped[str] = mapped_column(String(32), default="active")
    license_expires_at: Mapped[date] = mapped_column(Date)
    destination_attribution_enabled: Mapped[bool] = mapped_column(Boolean, default=False)

    users: Mapped[list["UserAccount"]] = relationship(back_populates="tenant")
    invoices: Mapped[list["Invoice"]] = relationship(back_populates="tenant")
    tickets: Mapped[list["Ticket"]] = relationship(back_populates="tenant")
    routers: Mapped[list["RouterDevice"]] = relationship(back_populates="tenant")
    resellers: Mapped[list["Reseller"]] = relationship(back_populates="tenant")


class UserAccount(TimestampMixin, Base):
    __tablename__ = "user_accounts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tenant_id: Mapped[int] = mapped_column(ForeignKey("tenants.id"), index=True)
    username: Mapped[str] = mapped_column(String(80), index=True)
    full_name: Mapped[str] = mapped_column(String(160))
    mobile: Mapped[str | None] = mapped_column(String(32), nullable=True)
    role: Mapped[str] = mapped_column(String(32), default="subscriber")
    status: Mapped[str] = mapped_column(String(32), default="active")
    service_name: Mapped[str] = mapped_column(String(120))
    wallet_balance: Mapped[Decimal] = mapped_column(Numeric(14, 2), default=0)
    is_online: Mapped[bool] = mapped_column(Boolean, default=False)
    assigned_ip: Mapped[str | None] = mapped_column(String(64), nullable=True)
    nas_name: Mapped[str | None] = mapped_column(String(120), nullable=True)
    online_since: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    download_bytes: Mapped[int] = mapped_column(Integer, default=0)
    upload_bytes: Mapped[int] = mapped_column(Integer, default=0)

    tenant: Mapped[Tenant] = relationship(back_populates="users")
    invoices: Mapped[list["Invoice"]] = relationship(back_populates="user")
    tickets: Mapped[list["Ticket"]] = relationship(back_populates="user")


class Invoice(TimestampMixin, Base):
    __tablename__ = "invoices"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tenant_id: Mapped[int] = mapped_column(ForeignKey("tenants.id"), index=True)
    user_id: Mapped[int | None] = mapped_column(ForeignKey("user_accounts.id"), nullable=True)
    number: Mapped[str] = mapped_column(String(40), unique=True, index=True)
    item_name: Mapped[str] = mapped_column(String(180))
    amount: Mapped[Decimal] = mapped_column(Numeric(14, 2))
    status: Mapped[str] = mapped_column(String(32), default="open")
    issued_at: Mapped[date] = mapped_column(Date)

    tenant: Mapped[Tenant] = relationship(back_populates="invoices")
    user: Mapped[UserAccount | None] = relationship(back_populates="invoices")


class Ticket(TimestampMixin, Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tenant_id: Mapped[int] = mapped_column(ForeignKey("tenants.id"), index=True)
    user_id: Mapped[int | None] = mapped_column(ForeignKey("user_accounts.id"), nullable=True)
    subject: Mapped[str] = mapped_column(String(180))
    status: Mapped[str] = mapped_column(String(32), default="open")
    priority: Mapped[str] = mapped_column(String(32), default="normal")
    assigned_to: Mapped[str | None] = mapped_column(String(120), nullable=True)

    tenant: Mapped[Tenant] = relationship(back_populates="tickets")
    user: Mapped[UserAccount | None] = relationship(back_populates="tickets")
    messages: Mapped[list["TicketMessage"]] = relationship(back_populates="ticket")


class TicketMessage(TimestampMixin, Base):
    __tablename__ = "ticket_messages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ticket_id: Mapped[int] = mapped_column(ForeignKey("tickets.id"), index=True)
    author_type: Mapped[str] = mapped_column(String(32))
    message: Mapped[str] = mapped_column(Text)

    ticket: Mapped[Ticket] = relationship(back_populates="messages")


class RouterDevice(TimestampMixin, Base):
    __tablename__ = "router_devices"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tenant_id: Mapped[int] = mapped_column(ForeignKey("tenants.id"), index=True)
    name: Mapped[str] = mapped_column(String(120))
    device_type: Mapped[str] = mapped_column(String(80))
    ip_address: Mapped[str] = mapped_column(String(64))
    radius_status: Mapped[str] = mapped_column(String(32), default="unknown")
    accounting_status: Mapped[str] = mapped_column(String(32), default="unknown")
    status: Mapped[str] = mapped_column(String(32), default="active")

    tenant: Mapped[Tenant] = relationship(back_populates="routers")


class Reseller(TimestampMixin, Base):
    __tablename__ = "resellers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tenant_id: Mapped[int] = mapped_column(ForeignKey("tenants.id"), index=True)
    name: Mapped[str] = mapped_column(String(160))
    credit_balance: Mapped[Decimal] = mapped_column(Numeric(14, 2), default=0)
    sales_month: Mapped[Decimal] = mapped_column(Numeric(14, 2), default=0)
    commission_percent: Mapped[Decimal] = mapped_column(Numeric(5, 2), default=0)
    status: Mapped[str] = mapped_column(String(32), default="active")

    tenant: Mapped[Tenant] = relationship(back_populates="resellers")

