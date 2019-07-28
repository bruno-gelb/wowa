import click


@click.group()
def cli():
    pass


@cli.command()
@click.argument('addon_name')
def install(addon_name):
    click.echo(f'Installing {addon_name} (latest) ..')
    addon_version = '5.8.2'
    click.echo(f'Installed {addon_name}=={addon_version}.')


@cli.command()
@click.argument('addon_name')
def uninstall(addon_name):
    click.echo(f'Uninstalling {addon_name} (latest) ..')
    addon_version = '5.8.2'
    click.echo(f'Uninstalled {addon_name}=={addon_version}.')


@cli.command()
@click.argument('addon_name')
def upgrade(addon_name):
    click.echo(addon_name)


@cli.command(name='list')
@click.option('-i', '--installed', is_flag=True, default=False)
def list_addons(installed):
    print(installed)


@cli.command()
@click.argument('addon_name')
def version(addon_name):
    click.echo(addon_name)


@cli.command()
@click.argument('addon_name')
def search(addon_name):
    click.echo(addon_name)


@cli.command()
@click.argument('addon_name')
def info(addon_name):
    click.echo(addon_name)


if __name__ == '__main__':
    cli()
