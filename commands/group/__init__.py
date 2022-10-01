import click


@click.group(name="group", help="Manage groups")
def group_cmd():
    raise click.UsageError("This command hasn't been implemented yet")
