import click

from core.install import install
from core.list_installed import list_installed
from core.uninstall import uninstall
from core.utils import parse_name_version


@click.group()
@click.version_option()
def cli():
    pass


@cli.command(name='install')
@click.argument('addon_name')
def install_command(addon_name):
    click.echo(f'Installing {addon_name} (latest) ..')
    name, version = parse_name_version(addon_name)
    install(name, version)


@cli.command(name='uninstall')
@click.argument('addon_name')
def uninstall_command(addon_name):
    click.echo(f'Uninstalling {addon_name} (latest) ..')
    uninstall(addon_name)


@cli.command(name='upgrade')
@click.argument('addon_name')
def upgrade_command(addon_name):
    click.echo(addon_name)


@cli.command(name='list')
def list_command():
    list_installed()


@cli.command(name='version')
@click.argument('addon_name')
def version_command(addon_name):
    click.echo(addon_name)


@cli.command(name='search')
@click.argument('addon_name')
def search_command(addon_name):
    click.echo(addon_name)


@cli.command(name='info')
@click.argument('addon_name')
def info_command(addon_name):
    click.echo(addon_name)


if __name__ == '__main__':
    cli()
