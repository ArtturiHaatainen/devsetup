from devsetup.utils.environment import check_git, check_node, check_python,detect_os
import typer
from rich.console import Console
from rich.table import Table
console=Console()
def run_doctor():
    checks = [
        check_git(),
        check_python(),
        check_node(),
        detect_os()
    ]

    table = Table(title="DevSetup Doctor")

    table.add_column("Check")
    table.add_column("Result")

    for result in checks:
        if result.available:
            status = f"[green]✓[/green] {result.version}"
        else:
            status = "[red]✗[/red] Not installed"

        table.add_row(result.name, status)

    console.print(table)