from rich.console import Console
from rich.table import Table

console = Console()


def show(results):

    table = Table(title="OPTIONFORGE BROKER VALIDATION")

    table.add_column("Metric")
    table.add_column("Broker", justify="right")
    table.add_column("OptionForge", justify="right")
    table.add_column("Difference", justify="right")
    table.add_column("Status", justify="center")

    for r in results:

        status = "PASS" if r.passed else "FAIL"

        table.add_row(

            r.metric,

            f"{r.broker:.6f}",

            f"{r.optionforge:.6f}",

            f"{r.difference:.6f}",

            status,

        )

    console.print(table)