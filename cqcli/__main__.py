import logging
import os
import sys

import click

from cqcli import command, config, base_exception


def main():
    logging.debug('Welcome to cqclis.')
    os.makedirs(config.CONFIG_DIR, exist_ok=True)
    cmds = command.get_all_commands()
    if len(sys.argv) == 1:
        print('Nothing to do...')
        exit(0)
    else:
        cli = click.Group()
        for cmd in cmds:
            cli.add_command(cmd.click_cmd)
            logging.debug("Add command %s" % cmd.name)
        try:
            cli()
        except base_exception.BaseException as e:
            e.print_error_msg()
            e.print_help_msg()
            raise SystemExit(1)
        except Exception as e:
            is_solved = base_exception.try_to_handle_third_party_exception()
            if not is_solved:
                raise
            raise SystemExit(1)


if __name__ == '__main__':
    main()
