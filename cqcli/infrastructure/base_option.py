from abc import ABC
from typing import Tuple

import click


class BaseOption(ABC):
    def __init__(self, param: Tuple = None, default=None, help: str = None):
        self.param = param
        self.default = default
        self.help = help

    def click_option(self):
        return click.Option(param_decls=self.param, help=self.help, default=self.default)
