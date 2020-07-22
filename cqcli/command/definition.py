import inspect
import logging

import click


class Command(object):

    @property
    def click_command(self):
        """Returns a click core command object"""


class SingleActionCommand(Command):
    name = ''
    help_doc = ''

    def __init__(self):
        self._click_cmd = self._create_click_cmd()

    @property
    def options(self):
        """Returns the options list of the command"""

    @property
    def actions(self):
        """Returns the actions list of the command"""

    @property
    def click_cmd(self):
        return self._click_cmd

    def _create_click_cmd(self):
        logging.debug("Actions in cmd %s: %s", self.name, self.actions),
        def f(action, *args, **kwargs):
            for act in self.actions:
                if act.name == action:
                    self._current_action = act
                    ctx = click.get_current_context()
                    signature = inspect.signature(act.before)
                    params = {k: v for k, v in ctx.params.item() if k in signature.parameters}
                    act.before(**params)
                    signature = inspect.signature(act.run)
                    params = {k: v for k, v in ctx.params.item() if k in signature.parameters}
                    act.run(**params)
                    signature = inspect.signature(act.after)
                    params = {k: v for k, v in ctx.params.item() if k in signature.parameters}
                    act.after(**params)

        action_argument = click.core.Argument(param_decls=('action',))
        click.decorators._param_memo(f, action_argument)
        for option in self.options:
            click.decorators._param_memo(f, option)
        cmd = click.command(name=self.name)(f)
        return cmd


class SingleAction(object):
    name = ''
    help_doc = ''
    example_doc = []

    @property
    def options(self):
        """返回一个 click.core.Option 的列表，代表这个 action 使用的参数"""

    def before(self):
        """action 执行前的 hook"""

    def run(self):
        """action 具体的执行逻辑"""

    def after(self):
        """action 执行后的 hook"""
