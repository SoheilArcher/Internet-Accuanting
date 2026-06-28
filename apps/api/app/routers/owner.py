from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.models import Tenant
from app.schemas import TenantRead

router = APIRouter(prefix="/owner", tags=["owner"])


@router.get("/tenants", response_model=list[TenantRead])
async def list_tenants(session: AsyncSession = Depends(get_session)) -> list[Tenant]:
    result = await session.scalars(select(Tenant).order_by(Tenant.id))
    return list(result)

