from . import action, option
from ..base_command import BaseSingleActionCommand


class GrpcCommand(BaseSingleActionCommand):
    name = "grpc"
    help_doc = "gRPC相关操作"

    @property
    def actions(self):
        return action.ALL

    @property
    def options(self):
        return option.ALL


command = GrpcCommand()
