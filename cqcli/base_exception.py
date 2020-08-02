import click

third_party_exc_resolve_order = []


class BaseException(Exception):
    """Base class for exceptions"""

    def __init__(self, message):
        super().__init__()
        self.message = message

    def print_error_msg(self):
        """Output error message"""
        click.secho("Error:", fg="red")
        click.secho(self.message)

    def print_help_msg(self):
        """Output help message """


def try_to_handle_third_party_exception():
    """"""
