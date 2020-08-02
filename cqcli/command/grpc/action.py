from cqcli.command.grpc import option
from ..base_action import BaseAction


class Generate(BaseAction):
    name = "generate"
    help_msg = "生成gRPC api"
    example_doc = [
        ('-o/--output ./', '输出路径 ')
    ]

    @property
    def options(self):
        return option.ALL

    def run(self):
        print("Not implement")


ALL = [Generate()]
