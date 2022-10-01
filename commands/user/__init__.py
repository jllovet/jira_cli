import click
from .avatar import avatar_cmd
from .group import group_cmd

@click.group(name="user", help="Manage users")
def user_cmd():
    raise click.UsageError("This command hasn't been implemented yet")

user_cmd.add_command(avatar_cmd)
user_cmd.add_command(group_cmd)
