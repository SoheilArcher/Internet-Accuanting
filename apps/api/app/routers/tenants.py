from decimal import Decimal

from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.models import Invoice, Reseller, RouterDevice, Tenant, Ticket, TicketMessage, UserAccount
from app.schemas import (
    DashboardRead,
    DestinationRecord,
    InvoiceRead,
    ResellerRead,
    RouterRead,
    TicketCreate,
    TicketRead,
    UserCreate,
    UserRead,
)

router = APIRouter(prefix="/tenants/{tenant_id}", tags=["tenants"])


async def get_tenant_or_404(tenant_id: int, session: AsyncSession) -> Tenant:
    tenant = await session.get(Tenant, tenant_id)
    if tenant is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tenant not found")
    return tenant


def require_owner_access(request: Request) -> None:
    if request.headers.get("X-Platform-Owner") != "true":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Destination attribution is owner-only by default",
        )


@router.get("/dashboard", response_model=DashboardRead)
async def tenant_dashboard(tenant_id: int, session: AsyncSession = Depends(get_session)) -> DashboardRead:
    tenant = await get_tenant_or_404(tenant_id, session)
    users_total = await session.scalar(select(func.count()).select_from(UserAccount).where(UserAccount.tenant_id == tenant_id))
    users_online = await session.scalar(
        select(func.count()).select_from(UserAccount).where(UserAccount.tenant_id == tenant_id, UserAccount.is_online.is_(True))
    )
    invoices_open = await session.scalar(
        select(func.count()).select_from(Invoice).where(Invoice.tenant_id == tenant_id, Invoice.status == "open")
    )
    revenue_paid = await session.scalar(
        select(func.coalesce(func.sum(Invoice.amount), 0)).where(Invoice.tenant_id == tenant_id, Invoice.status == "paid")
    )
    tickets_open = await session.scalar(
        select(func.count()).select_from(Ticket).where(Ticket.tenant_id == tenant_id, Ticket.status != "closed")
    )
    routers_active = await session.scalar(
        select(func.count()).select_from(RouterDevice).where(RouterDevice.tenant_id == tenant_id, RouterDevice.status != "offline")
    )
    return DashboardRead(
        tenant=tenant,
        users_total=users_total or 0,
        users_online=users_online or 0,
        invoices_open=invoices_open or 0,
        revenue_paid=revenue_paid or Decimal("0"),
        tickets_open=tickets_open or 0,
        routers_active=routers_active or 0,
    )


@router.get("/users", response_model=list[UserRead])
async def list_users(tenant_id: int, session: AsyncSession = Depends(get_session)) -> list[UserAccount]:
    await get_tenant_or_404(tenant_id, session)
    result = await session.scalars(select(UserAccount).where(UserAccount.tenant_id == tenant_id).order_by(UserAccount.id))
    return list(result)


@router.post("/users", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(tenant_id: int, payload: UserCreate, session: AsyncSession = Depends(get_session)) -> UserAccount:
    await get_tenant_or_404(tenant_id, session)
    user = UserAccount(tenant_id=tenant_id, **payload.model_dump())
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


@router.get("/online-users", response_model=list[UserRead])
async def list_online_users(tenant_id: int, session: AsyncSession = Depends(get_session)) -> list[UserAccount]:
    await get_tenant_or_404(tenant_id, session)
    result = await session.scalars(
        select(UserAccount).where(UserAccount.tenant_id == tenant_id, UserAccount.is_online.is_(True)).order_by(UserAccount.username)
    )
    return list(result)


@router.get("/invoices", response_model=list[InvoiceRead])
async def list_invoices(tenant_id: int, session: AsyncSession = Depends(get_session)) -> list[Invoice]:
    await get_tenant_or_404(tenant_id, session)
    result = await session.scalars(select(Invoice).where(Invoice.tenant_id == tenant_id).order_by(Invoice.id.desc()))
    return list(result)


@router.get("/tickets", response_model=list[TicketRead])
async def list_tickets(tenant_id: int, session: AsyncSession = Depends(get_session)) -> list[Ticket]:
    await get_tenant_or_404(tenant_id, session)
    result = await session.scalars(select(Ticket).where(Ticket.tenant_id == tenant_id).order_by(Ticket.id.desc()))
    return list(result)


@router.post("/tickets", response_model=TicketRead, status_code=status.HTTP_201_CREATED)
async def create_ticket(tenant_id: int, payload: TicketCreate, session: AsyncSession = Depends(get_session)) -> Ticket:
    await get_tenant_or_404(tenant_id, session)
    ticket = Ticket(
        tenant_id=tenant_id,
        user_id=payload.user_id,
        subject=payload.subject,
        priority=payload.priority,
        status="open",
    )
    session.add(ticket)
    await session.flush()
    session.add(TicketMessage(ticket_id=ticket.id, author_type="subscriber", message=payload.message))
    await session.commit()
    await session.refresh(ticket)
    return ticket


@router.get("/routers", response_model=list[RouterRead])
async def list_routers(tenant_id: int, session: AsyncSession = Depends(get_session)) -> list[RouterDevice]:
    await get_tenant_or_404(tenant_id, session)
    result = await session.scalars(select(RouterDevice).where(RouterDevice.tenant_id == tenant_id).order_by(RouterDevice.id))
    return list(result)


@router.get("/resellers", response_model=list[ResellerRead])
async def list_resellers(tenant_id: int, session: AsyncSession = Depends(get_session)) -> list[Reseller]:
    await get_tenant_or_404(tenant_id, session)
    result = await session.scalars(select(Reseller).where(Reseller.tenant_id == tenant_id).order_by(Reseller.id))
    return list(result)


@router.get("/attribution/destinations", response_model=list[DestinationRecord])
async def destination_report(tenant_id: int, request: Request, session: AsyncSession = Depends(get_session)) -> list[DestinationRecord]:
    await get_tenant_or_404(tenant_id, session)
    require_owner_access(request)
    return [
        DestinationRecord(
            username="mohsen-021",
            assigned_ip="10.8.12.44",
            destination="example-service.net",
            destination_port=443,
            protocol="tcp",
            nas_name="NAS-Tehran",
            confidence="high",
        )
    ]
