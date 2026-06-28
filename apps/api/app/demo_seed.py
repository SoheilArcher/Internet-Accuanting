from datetime import date, datetime, timezone
from decimal import Decimal

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Invoice, Reseller, RouterDevice, Tenant, Ticket, TicketMessage, UserAccount


async def seed_demo_data(session: AsyncSession) -> None:
    existing = await session.scalar(select(Tenant.id).limit(1))
    if existing is not None:
        return

    tenant = Tenant(
        name="اپراتور شرق",
        status="active",
        license_expires_at=date(2027, 6, 27),
        destination_attribution_enabled=False,
    )
    session.add(tenant)
    await session.flush()

    users = [
        UserAccount(
            tenant_id=tenant.id,
            username="mohsen-021",
            full_name="محسن رضایی",
            mobile="09120000001",
            service_name="PPPoE 100GB",
            wallet_balance=Decimal("1200000"),
            is_online=True,
            assigned_ip="10.8.12.44",
            nas_name="NAS-Tehran",
            online_since=datetime(2026, 6, 28, 8, 42, tzinfo=timezone.utc),
            download_bytes=5_153_960_755,
            upload_bytes=650_117_120,
        ),
        UserAccount(
            tenant_id=tenant.id,
            username="sara-vpn",
            full_name="سارا احمدی",
            mobile="09120000002",
            service_name="VPN Pro",
            wallet_balance=Decimal("3200000"),
            is_online=True,
            assigned_ip="10.9.3.11",
            nas_name="VPN-Node-2",
            online_since=datetime(2026, 6, 28, 9, 18, tzinfo=timezone.utc),
            download_bytes=1_288_490_188,
            upload_bytes=220_200_960,
        ),
        UserAccount(
            tenant_id=tenant.id,
            username="ali-home",
            full_name="علی کریمی",
            mobile="09120000003",
            service_name="ADSL 250GB",
            wallet_balance=Decimal("0"),
            status="expired",
        ),
    ]
    session.add_all(users)
    await session.flush()

    session.add_all(
        [
            Invoice(
                tenant_id=tenant.id,
                user_id=users[0].id,
                number="INV-20391",
                item_name="PPPoE 100GB - تمدید",
                amount=Decimal("2400000"),
                status="paid",
                issued_at=date(2026, 6, 28),
            ),
            Invoice(
                tenant_id=tenant.id,
                user_id=users[1].id,
                number="INV-20390",
                item_name="VPN Pro یک‌ساله",
                amount=Decimal("6800000"),
                status="paid",
                issued_at=date(2026, 6, 28),
            ),
            Invoice(
                tenant_id=tenant.id,
                user_id=None,
                number="INV-20388",
                item_name="IP ثابت + سرویس سازمانی",
                amount=Decimal("18500000"),
                status="open",
                issued_at=date(2026, 6, 27),
            ),
        ]
    )

    ticket = Ticket(
        tenant_id=tenant.id,
        user_id=users[0].id,
        subject="کندی سرویس شبانه",
        status="open",
        priority="normal",
        assigned_to="پشتیبان ۱",
    )
    session.add(ticket)
    await session.flush()
    session.add(
        TicketMessage(
            ticket_id=ticket.id,
            author_type="subscriber",
            message="از ساعت ۸ شب به بعد سرعت خیلی کم می‌شود.",
        )
    )

    session.add_all(
        [
            RouterDevice(
                tenant_id=tenant.id,
                name="NAS-Tehran",
                device_type="MikroTik CCR",
                ip_address="172.22.78.13",
                radius_status="ok",
                accounting_status="ok",
                status="online",
            ),
            RouterDevice(
                tenant_id=tenant.id,
                name="BRAS-Mashhad",
                device_type="Huawei BRAS",
                ip_address="10.20.0.2",
                radius_status="ok",
                accounting_status="delay",
                status="warning",
            ),
        ]
    )

    session.add_all(
        [
            Reseller(
                tenant_id=tenant.id,
                name="Reseller Babak",
                credit_balance=Decimal("500000000"),
                sales_month=Decimal("1200000000"),
                commission_percent=Decimal("18"),
            ),
            Reseller(
                tenant_id=tenant.id,
                name="Reseller Moridi",
                credit_balance=Decimal("140000000"),
                sales_month=Decimal("480000000"),
                commission_percent=Decimal("12"),
                status="low_credit",
            ),
        ]
    )

    await session.commit()

