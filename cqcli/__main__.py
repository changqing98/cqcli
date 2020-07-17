import os

from cqcli import command, config


def main():
    print("Welcome to cqzone.")
    os.makedirs(config.CONFIG_DIR, exist_ok=True)
    cmds = command.get_all_commands()
    print(cmds)


if __name__ == '__main__':
    main()
