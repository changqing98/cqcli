import os

from cqcli.service.grpc.generator.base import BaseGenerator


class Generator(BaseGenerator):
    @staticmethod
    def run():
        cmd = f'protoc --go_out=plugins=grpc:grpc-go ./*.proto'
        os.system(cmd)
