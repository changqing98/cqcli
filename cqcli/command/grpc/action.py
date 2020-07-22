from cqcli.command.definition import SingleAction
from cqcli.command.grpc import option


class Generate(SingleAction):
    name = "generate"
    help_msg = "生成gRPC api"
    example_doc = []

    @property
    def options(self):
        return option.ALL

    def run(self):
        print("Not implement")


ALL = [Generate()]
