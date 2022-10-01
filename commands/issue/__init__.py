import click
from .attachment import attachment_cmd
from .worklog import worklog_cmd
from .label import label_cmd
from .field import field_cmd
from .watcher import watcher_cmd


@click.group(name="issue", help="Manage issues")
def issue_cmd():
    raise click.UsageError("This command hasn't been implemented yet")


issue_cmd.add_command(attachment_cmd)
issue_cmd.add_command(worklog_cmd)
issue_cmd.add_command(label_cmd)
issue_cmd.add_command(field_cmd)
issue_cmd.add_command(watcher_cmd)
