from abc import ABC, abstractmethod
from typing import List

from cqcli.infrastructure.base_option import BaseOption


class BaseAction(ABC):
    name = ''
    example_doc = ''
    help_doc = ''

    @property
    @abstractmethod
    def options(self) -> List[BaseOption]:
        """Returns options of this option"""

    @abstractmethod
    def run(self, **kwargs):
        """The actual logic of this action"""
