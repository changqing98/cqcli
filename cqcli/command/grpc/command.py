from . import action, option
from ...infrastructure.base_command import BaseCommand


class GrpcBaseCommand(BaseCommand):
    name = "grpc"
    help_doc = "gRPC相关操作"

    @property
    def actions(self):
        return action.ALL

    @property
    def options(self):
        return option.ALL


command = GrpcBaseCommand()
