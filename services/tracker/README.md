### Creating session

uv run src/tracker/database/session.py

### Adding table to database

src/tracker/database/models.py

class Benchmark(SQLModel, table=True):
id: UUID | None = Field(default_factory=uuid4, primary_key=True)
name: str
started_at: datetime = Field(default_factory=datetime.now)
finished_at: datetime | None = None
...

src/tracker/database/session.py

from src.tracker.database.models import Benchmark, EvaluationResult, Task

\_exposed_models: list[type[SQLModel]] = [Benchmark, EvaluationResult, Task]

uv run src/tracker/database/session.py

### Testing database

[Documentation](https://sqlmodel.tiangolo.com/tutorial/fastapi/tests/?h=#testing-database)
