from cqcli.command.definition import SingleAction
from cqcli.command.grpc import option


class TestAction(SingleAction):
    name = "test"
    help_msg = "Test action"
    example_doc = []

    @property
    def options(self):
        return option.ALL

    def run(self):
        print("Not implement")


ALL = [TestAction()]
