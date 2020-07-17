from ..definition import Command
from . import action, option


class GrpcCommand(Command):
    name = "grpc"
    help_doc = "GRPC相关操作"

    @property
    def actions(self):
        return action.ALL

    @property
    def options(self):
        return option.ALL


command = GrpcCommand()
