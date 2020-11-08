from cqcli.command.grpc import option
from cqcli.infrastructure.base_action import BaseAction


class Generate(BaseAction):
    name = "generate"
    help_msg = "生成gRPC api"
    example_doc = [
        ('-o/--output ./', '输出路径 ')
    ]

    @property
    def options(self):
        return option.ALL

    def run(self, version):
        print(f'Do generate, version: {version}')


ALL = [Generate()]
