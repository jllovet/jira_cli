import click
from .attachment import attachment_cmd


@click.group(name="issue", help="Manage issues")
def issue_cmd():
    pass


issue_cmd.add_command(attachment_cmd)
