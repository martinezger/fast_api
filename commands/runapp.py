import click
import uvicorn

from app import create_app
from config import DevConfig, QaConfig, ProdConfig, config_factory


@click.command()
@click.argument('environment', nargs=1)
def cli(environment):
    """
        Run application with a given environment.
        ex: runapp qa
    """
    try:
        config = config_factory(environment)
        click.echo(f"running {environment} enviroment")
        uvicorn.run(create_app(config), host=config.HOST, port=config.PORT)
    except ValueError as e:
        click.echo(e.message)