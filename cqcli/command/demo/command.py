from . import action, option
from ..base_command import BaseSingleActionCommand


class DemoCommand(BaseSingleActionCommand):
    name = "demo"
    help_doc = "Demo command"

    @property
    def actions(self):
        return action.ALL

    @property
    def options(self):
        return option.ALL


command = DemoCommand()
