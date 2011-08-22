import sys

from codereview.commands import commands
from codereview.fatal import fatal

def run_command(command_name, args):
    """Run the command with the provided arguments."""
    try:
        cmd = commands[command_name]
    except KeyError:
        fatal('Invalid command: %s' % command_name)

    cmd(*args)

