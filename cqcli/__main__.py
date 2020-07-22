import os
import sys
import logging
import click

from cqcli import command, config, error


def main():
    print('Welcome to cqzone.')
    os.makedirs(config.CONFIG_DIR, exist_ok=True)
    cmds = command.get_all_commands()
    if len(sys.argv) == 1:
        print('Nothing to do...')

    else:
        cli = click.Group()
        for cmd in cmds:
            logging.debug("Add command:%s", cmd)
            cli.add_command(cmd.click_cmd())

        try:
            cli()
        except error.CqcliError as e:
            e.print_error_msg()
            e.print_help_msg()
            raise SystemExit(1)
        except Exception as e:
            is_solved = error.try_to_handle_third_party_exception(e)
            if not is_solved:
                raise
            raise SystemExit(1)


if __name__ == '__main__':
    main()
