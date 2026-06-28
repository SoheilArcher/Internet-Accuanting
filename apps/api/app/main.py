from contextlib import asynccontextmanager
from collections.abc import AsyncGenerator

from fastapi import FastAPI

from app.core.config import get_settings
from app.db import SessionLocal, init_db
from app.demo_seed import seed_demo_data
from app.routers.health import router as health_router
from app.routers.owner import router as owner_router
from app.routers.tenants import router as tenants_router


def create_app() -> FastAPI:
    settings = get_settings()

    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
        await init_db()
        if settings.seed_demo_data:
            async with SessionLocal() as session:
                await seed_demo_data(session)
        yield

    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        lifespan=lifespan,
    )

    app.include_router(health_router, prefix=settings.api_prefix)
    app.include_router(owner_router, prefix=settings.api_prefix)
    app.include_router(tenants_router, prefix=settings.api_prefix)
    return app


app = create_app()
