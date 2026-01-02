.PHONY: help install test test-integration test-all style style-check typecheck \
	tracker-install tracker-dev \
	swebench-install swebench-dev \
	validate-workspace

PYTHON_VERSION := 3.11
SWEBENCH_PYTHON_VERSION := 3.12

TRACKER_PORT ?= 8000
SWEBENCH_PORT ?= 8001

help:
	@echo "Makefile for agentic-harness"
	@echo ""
	@echo "Setup:"
	@echo "  make install             Install root workspace dependencies"
	@echo "  make tracker-install     Install tracker service (separate venv)"
	@echo "  make swebench-install    Install swebench service (separate venv)"
	@echo ""
	@echo "Development:"
	@echo "  make style               Lint & Format"
	@echo "  make style-check         Check style"
	@echo "  make typecheck           Typecheck"
	@echo "  make validate-workspace  Check all workspace packages are in sync"
	@echo ""
	@echo "Services (development mode):"
	@echo "  make tracker-dev         Start tracker service on port $(TRACKER_PORT)"
	@echo "  make swebench-dev        Start swebench service on port $(SWEBENCH_PORT)"

install:
	uv venv --python $(PYTHON_VERSION)
	uv cache clean model-library valsai
	uv sync --group dev
	@echo "🎉 Done! Run 'source .venv/bin/activate' to activate the environment locally."

update-submodules:
	git submodule update --remote --merge
	uv sync

venv_check:
	@if [ ! -f .venv/bin/activate ]; then \
		echo "❌ Virtualenv not found! Run \`make install\` first."; \
		exit 1; \
	fi

format: venv_check
	@uv run ruff format .

lint: venv_check
	@uv run ruff check --fix .

style: format lint

style-check: venv_check
	@uv run ruff format --check .
	@uv run ruff check .

typecheck: venv_check
	@uv run basedpyright

validate-workspace:
	@echo "Validating workspace is in sync..."
	@uv sync --all-packages --dry-run > /dev/null 2>&1 && echo "✓ All workspace packages are synced" || (echo "❌ Workspace out of sync! Run 'uv sync --all-packages'" && exit 1)

# Service commands
tracker-install:
	@echo "Installing tracker service (separate venv)..."
	@cd services/tracker && uv venv --python $(PYTHON_VERSION)
	@cd services/tracker && uv sync
	@echo "✓ Tracker service installed at services/tracker/.venv"

tracker-dev:
	@echo "Starting tracker service (development mode on port $(TRACKER_PORT))..."
	@cd services/tracker && uv run fastapi dev main.py --port $(TRACKER_PORT)

swebench-install:
	@echo "Installing swebench service (separate venv)..."
	@cd services/benchmarks/swebench && uv venv --python $(SWEBENCH_PYTHON_VERSION)
	@cd services/benchmarks/swebench && uv sync
	@echo "✓ SWE-bench service installed at services/benchmarks/swebench/.venv"

swebench-dev:
	@echo "Starting swebench service (development mode on port $(SWEBENCH_PORT))..."
	@cd services/benchmarks/swebench && uv run fastapi dev main.py --port $(SWEBENCH_PORT)
