import importlib
import os

from cqcli.infrastructure.base_command import BaseCommand


def get_all_commands() -> list:
    cmds = []
    this_dir = os.path.dirname(os.path.realpath(__file__))
    for filename in os.listdir(this_dir):
        if os.path.isdir(os.path.join(this_dir, filename)):
            module = importlib.import_module(f"{__package__}.{filename}")
            if hasattr(module, "command") and isinstance(module.command, BaseCommand):
                cmds.append(module.command)
    return cmds
