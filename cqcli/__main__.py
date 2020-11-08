import logging
import os
import sys

import click

from cqcli import command, config


def main():
    logging.debug('Welcome to cqcli.')
    os.makedirs(config.CONFIG_DIR, exist_ok=True)
    cmds = command.get_all_commands()
    if len(sys.argv) == 1:
        print('Nothing to do...')
        exit(0)
    else:
        cli = click.Group()
        for cmd in cmds:
            cli.add_command(cmd.click_command())
            logging.debug("Add command %s" % cmd.name)
        cli()


if __name__ == '__main__':
    main()
