import click
from .attachment import attachment_cmd


@click.group(name="issue", help="Manage issues")
def issue_cmd():
    raise click.UsageError("This command hasn't been implemented yet")


issue_cmd.add_command(attachment_cmd)
