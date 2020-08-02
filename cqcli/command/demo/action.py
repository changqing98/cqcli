from ..base_action import BaseAction
from . import option


class TestAction(BaseAction):
    name = "test"
    help_doc = "Test action"
    example_doc = [
        ('-n/--name demo', "姓名")
    ]

    @property
    def options(self):
        return option.ALL

    def run(self, name):
        print("This is test action", name)


ALL = [TestAction()]
