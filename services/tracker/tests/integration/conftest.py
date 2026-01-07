from collections.abc import Generator
from typing import Any

import pytest
from sqlmodel import Session, SQLModel, StaticPool, create_engine
from tracker.database.models import *  # noqa: F403


@pytest.fixture(scope="function")
def database_session() -> Generator[Session, Any, None]:
    """Create an in-memory database and mock the session engine."""
    test_engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)

    SQLModel.metadata.create_all(test_engine)

    with Session(test_engine) as session:
        yield session

    SQLModel.metadata.drop_all(test_engine)
