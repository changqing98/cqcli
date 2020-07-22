import os

from .base_generator import BaseGenerator

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


class JavaGenerator(BaseGenerator):
    def __init__(self, args):
        super().__init__(args)
        self.jar = f"{self.fullname}.jar"
        self.template_src = self.get_template_src()
        self.output_path = self.get_output_path()

    def generate(self):
        cmd = f""

    def get_tmp_path(self):
        tmp_path = "/tmp/cqcli/grpc"
        if not os.path.exists(tmp_path):
            os.system(f"mkdir -p {tmp_path}")
        return tmp_path

    def copy_protos(self):
        os.system()

    def get_template_src(self):
        return f"{CURRENT_PATH}/templates/java"

    def get_output_path(self):
        return "./"
