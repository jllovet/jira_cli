import click

from commands import command_groups


@click.group()
def cli():
    pass


for command in command_groups:
    cli.add_command(command, command.name)

if __name__ == "__main__":
    cli()
