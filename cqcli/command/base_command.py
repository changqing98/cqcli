import abc
import inspect
import itertools
import logging

import click

_HELP_DOC_TEMPLATE = """
{cmd_doc}
"""


class BaseCommand:

    @property
    @abc.abstractmethod
    def click_cmd(self):
        """Returns a click core command object"""


class BaseSingleActionCommand(BaseCommand):
    name = ''
    help_doc = ''

    def __init__(self):
        self._click_cmd = self._create_click_cmd()

    @property
    @abc.abstractmethod
    def options(self):
        """Returns all options of this command"""

    @property
    @abc.abstractmethod
    def actions(self):
        """Returns all actions of this action"""

    @property
    def click_cmd(self):
        return self._click_cmd

    def _create_click_cmd(self):
        """Creates click cmd"""
        logging.debug("")

        def f(action, *args, **kwargs):
            for act in self.actions:
                if act.name == action:
                    self._current_action = act
                    ctx = click.get_current_context()
                    signature = inspect.signature(act.run)
                    params = {k: v for k, v in ctx.params.items() if k in signature.parameters}
                    act.run(**params)

        # Register arguments
        action_argument = click.core.Argument(param_decls=('action',))
        click.decorators._param_memo(f, action_argument)
        # Register options
        for option in self.options:
            click.decorators._param_memo(f, option)

        context_settins = {
            'max_content_width': 800,
        }
        cmd = click.command(name=self.name, context_settings=context_settins)(f)
        # Generate the docs
        action_tpl = '  {:%s}{}' % (4 + max([len(action.name) for action in self.actions]))
        action_doc = '\n'.join([action_tpl.format(_.name, _.help_doc) for _ in self.actions])

        example_tuples = list(itertools.chain(*[
            [('cqcli {} {} {}'.format(self.name, action.name, cmd), doc) for cmd, doc in action.example_doc]
            for action in self.actions if action.example_doc
        ]))
        example_tpl = '{}:\n\n$ {}\n'
        example_doc = '\n'.join([example_tpl.format(doc, cmd) for cmd, doc in example_tuples])
        cmd.help = _HELP_DOC_TEMPLATE.format(
            cmd_doc=self.help_doc,
            action_doc=action_doc,
            example_doc=example_doc
        )
        return cmd
