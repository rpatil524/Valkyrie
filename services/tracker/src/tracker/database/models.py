from datetime import datetime
from enum import Enum
from typing import Any
from uuid import UUID, uuid4
from zoneinfo import ZoneInfo

from sqlmodel import JSON, Column, Field, SQLModel


class BenchmarkStatus(str, Enum):
    IN_PROGRESS = "in_progress"
    FINISHED = "finished"


class TaskStatus(str, Enum):
    STARTING = "starting"
    IN_PROGRESS = "in_progress"
    EVALUATING = "evaluating"
    FINISHED = "finished"


class Benchmark(SQLModel, table=True):
    id: UUID | None = Field(default_factory=uuid4, primary_key=True)
    name: str
    started_at: datetime = Field(default_factory=lambda: datetime.now(ZoneInfo("UTC")))
    finished_at: datetime | None = None
    status: BenchmarkStatus = Field(default=BenchmarkStatus.IN_PROGRESS)


class Task(SQLModel, table=True):
    id: UUID | None = Field(default_factory=uuid4, primary_key=True)
    task_id: UUID = Field(unique=True)
    status: TaskStatus = Field(default=TaskStatus.STARTING)
    started_at: datetime = Field(default_factory=lambda: datetime.now(ZoneInfo("UTC")))
    finished_at: datetime | None = None
    benchmark_id: UUID = Field(foreign_key="benchmark.id")


class EvaluationResult(SQLModel, table=True):
    id: UUID | None = Field(default_factory=uuid4, primary_key=True)
    task_id: UUID = Field(foreign_key="task.id")
    instance_id: str = Field(unique=True)
    result: dict[str, Any] = Field(default_factory=dict, sa_column=Column(JSON, nullable=False))
