import click
import uvicorn

from app import create_app


@click.command()
def cli():
    click.echo("running dev app")
    uvicorn.run(create_app(), host="0.0.0.0", port=8001)
