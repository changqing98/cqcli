import click


class CqcliError(object):
    """Base class for exceptions"""

    def __init__(self, message):
        super().__init__()
        self.message = message

    def display_error_msg(self):
        """Output error message"""
        click.secho("Error:", fg="red")
        click.secho(self.message)

    def print_help_msg(self):
        """Output help message """
