"""
Command line interface (CLI) frontend
"""

# Try using the built-in arparse if Python 2.7 or later.
# Otherwise fallback to our bundled version.
try: import argparse
except ImportError: import codereview.argparse as argparse

import codereview.commands as commands

def parse_arguments():
    """Parse command line arguments and option flags."""
    # Top-level parser
    parser = argparse.ArgumentParser(description='Code Review via Github')

    # Create sub-parser collection for the commands.
    subparsers = parser.add_subparsers(help='sub-command help')

    ### Commands

    # list --state=<state>
    list_parser = subparsers.add_parser('list', help='list help')
    list_parser.add_argument('--state', default='open', choices=('open', 'closed'))
    list_parser.set_defaults(subcommand=lambda args: commands.list(state=args.state))

    # show <id>
    show_parser = subparsers.add_parser('show', help='show help')
    show_parser.add_argument('id', type=int)
    show_parser.set_defaults(subcommand=lambda args: commands.show(ID=args.id))

    return parser.parse_args()

def main():
    # Parse command line arguments.
    # We also use the argument parser for determining which
    # sub-command will be executed.
    args = parse_arguments()

    # Dispatch to the subcommand.
    # The actual command is executed with in a lambda function.
    # This lambda passes argument variables to the command function.
    args.subcommand(args)    

