"""CLI views/commands for the agentic harness."""

from pathlib import Path

import click

from agentic_harness.cli.utils import upload_to_tracker


@click.group()
def cli():
    """Agentic Harness CLI."""
    pass


@cli.command()
@click.option(
    "--agent",
    type=click.Path(exists=True, path_type=Path),
    required=True,
    help="Path to agent submodule directory (e.g., submodules/claude_code)",
)
@click.option(
    "--contract",
    type=click.Path(exists=True, path_type=Path),
    required=True,
    help="Path to agent contract file (e.g., contracts/claude_code.py)",
)
@click.option(
    "--benchmark",
    type=str,
    required=True,
    help="Name of the benchmark to run (e.g., swebench, finance)",
)
def run(
    agent: Path,
    contract: Path,
    benchmark: str,
):
    """
    Run an agent on a benchmark.

    Example:
        harness run --agent submodules/claude_code --contract contracts/claude_code.py --benchmark swebench
    """
    click.echo(f"Running benchmark: {benchmark}")
    click.echo(f"Agent: {agent}")
    click.echo(f"Contract: {contract}")
    click.echo()

    upload_to_tracker(agent, contract)

    # TODO: Implement actual benchmark execution
    click.echo("\n[TODO] Execute benchmark with agent and contract")


if __name__ == "__main__":
    cli()
