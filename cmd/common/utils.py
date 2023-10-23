import shlex

import sh
from termcolor import cprint


def run_cmd(command_str, cwd=None, quiet=False):
    if not quiet:
        cprint(f"--> exec: {command_str}", 'grey')
    cmd, *args = shlex.split(command_str)
    sh.Command(cmd)(*args, _fg=True)
