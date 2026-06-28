import os
from pathlib import Path

import pytest
from fastapi.testclient import TestClient


@pytest.fixture()
def client(tmp_path: Path) -> TestClient:
    db_path = tmp_path / "test_accounting.db"
    os.environ["ACCOUNTING_DATABASE_URL"] = f"sqlite+aiosqlite:///{db_path.as_posix()}"
    os.environ["ACCOUNTING_SEED_DEMO_DATA"] = "true"

    from app.main import create_app

    app = create_app()
    with TestClient(app) as test_client:
        yield test_client

