import click

@click.command(name="issue", help="Manage issues")
def issue_cmd():
    raise click.UsageError("This command hasn't been implemented yet")
