from abc import ABCMeta


class BaseGenerator(metaclass = ABCMeta):
    def __init__(self, args):
        self.version = args.version
        self.name = args.name
        self.fullname = f"{self.name}-{self.version}"
        self.source = args.source
        self.output_path = args.output_path
        self.template_src = args.template_src
        self.tmp_workspace = args.tmp_workspace

    def generate(self):
        """开始生成gRPC API
        """
        pass