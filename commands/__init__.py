import click
from .user import user_cmd
from .group import group_cmd
from .board import board_cmd
from .issue import issue_cmd
from .project import project_cmd
from .sprint import sprint_cmd

command_groups = [
    user_cmd,
    group_cmd,
    board_cmd,
    issue_cmd,
    project_cmd,
    sprint_cmd
]
