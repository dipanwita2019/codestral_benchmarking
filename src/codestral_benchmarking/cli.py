"""Console script for codestral_benchmarking."""
import codestral_benchmarking

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for codestral_benchmarking."""
    console.print("Replace this message by putting your code into "
               "codestral_benchmarking.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
