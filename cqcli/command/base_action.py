import abc


class BaseAction:
    name = 'BaseAction'
    help_doc = 'Help document'
    example_doc = [
        ('-h/--help xxx', "Help")
    ]

    @property
    @abc.abstractmethod
    def options(self):
        """Returns options of this option"""

    @abc.abstractmethod
    def run(self):
        """The actual logic of this action"""
