import logging
from unittest import TestCase

from cqcli import command


class Test(TestCase):
    def test_get_all_commands(self):
        cmds = command.get_all_commands()
        logging.info("Cmds: %s" % [cmd.name for cmd in cmds])
        self.assertEquals(['demo', 'grpc'], [cmd.name for cmd in cmds])
