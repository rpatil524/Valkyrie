# Agentic Harness

Define your agent in `agents/`, add benchmarks as git submodules in `benchmarks/`, and run evaluations.

```bash
python runner.py --config config/ioi.yaml
```

**Setup:** `make install`
**Style:** `make style`

## Virtual Environment Setup

This project uses separate virtual environments for different components:

- **Root workspace** (`.venv`): Contains the main harness framework and shared dependencies
  - Install with: `make install`
  
- **Services** (isolated venvs): Each service maintains its own virtual environment. You might have to switch your venv depending on the service you are working on.
  - Tracker service: `make tracker-install` (creates `services/tracker/.venv`)
  - SWE-bench service: `make swebench-install` (creates `services/benchmarks/swebench/.venv`)

### Running Services

```bash
# Start tracker service (development mode)
make tracker-dev

# Start swebench service (development mode)
make swebench-dev
```

Each service uses only the dependencies declared in its own `pyproject.toml`.

### Additional setup steps

if you are developing locally and need to test changes to the sdk

comment out the ssh url to the sdk and use the generic dependency

_under dependencies_

```
# "valsai @ git+ssh://git@github.com/vals-ai/platform-be.git@dev#subdirectory=sdk",
  "valsai",
  ...
```

fill out the path to your local sdk version inside of `pyproject.toml`

```
[tool.uv.sources]
valsai = { path = "path/to/your/platform-be/sdk" }
```

We are using the privated model-proxy now in case we need to make changes while we develop. We are overriding the package version because the sdk version uses the public version of the model-library which would cause a conflict if we did not do this

```
[tool.uv]
override-dependencies = [
  "model-library @ git+https://github.com/vals-ai/model-proxy.git@dev",
]
```

Update the required python package version at the top

```
requires-python = ">=3.13"
```

After that you will need to reinstall the dependencies

```
# Use this command below to reinstall packages
uv sync --reinstall-package package name, ex. model-library
```
