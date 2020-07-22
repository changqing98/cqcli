from . import action, option
from ..definition import SingleActionCommand


class DemoCommand(SingleActionCommand):
    name = "demo"
    help_doc = "Demo command"

    @property
    def actions(self):
        return action.ALL

    @property
    def options(self):
        return option.ALL


command = DemoCommand()
