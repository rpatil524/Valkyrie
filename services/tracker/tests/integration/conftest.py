import pytest
from pytest import MonkeyPatch
from sqlmodel import Session, SQLModel, create_engine, inspect


@pytest.fixture(scope="function")
def database_session(monkeypatch: MonkeyPatch):
    """Create an in-memory database and mock the session engine."""
    test_engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})

    SQLModel.metadata.create_all(test_engine)

    monkeypatch.setattr("src.tracker.database.session.engine", test_engine)

    inspector = inspect(test_engine)
    tables = inspector.get_table_names()

    if not tables:
        pytest.fail("No tables found in database, failed to create tables")

    with Session(test_engine) as session:
        yield session

    SQLModel.metadata.drop_all(test_engine)

    test_engine.dispose()
