import click


@click.command(name="user", help="Manage users")
def user_cmd():
    raise click.UsageError("This command hasn't been implemented yet")
