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
@click.argument('addon_names', nargs=-1, required=True)
def install_command(addon_names):
    if isinstance(addon_names, str):
        addon_names = [addon_names]

    for addon_name in addon_names:
        click.echo()
        click.echo('Installing ' + click.style(addon_name, fg='yellow') + ' (latest) ..')
        name, version = parse_name_version(addon_name)
        install(name, version)


@cli.command(name='uninstall')
@click.argument('addon_names', nargs=-1, required=False)
def uninstall_command(addon_names):
    if isinstance(addon_names, str):
        addon_names = [addon_names]
    if not addon_names:
        addon_names = list_installed()
    for addon_name in addon_names:
        click.echo('Uninstalling ' + click.style(addon_name, fg='yellow') + ' (latest) ..')
        uninstall(addon_name)
    click.echo(click.style('All uninstalled.', bold=True))


@cli.command(name='upgrade')
@click.argument('addon_names', nargs=-1, required=False)
def upgrade_command(addon_names):
    if isinstance(addon_names, str):
        addon_names = [addon_names]
    for addon_name in addon_names:
        click.echo(addon_name)


@cli.command(name='list')
def list_command():
    installed = list_installed()
    for addon, addon_data in installed.items():
        click.echo(click.style(addon, fg='yellow') + '==' + addon_data)


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
