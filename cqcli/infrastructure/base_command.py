import inspect
from abc import ABC, abstractmethod
from typing import List

import click

from cqcli.infrastructure.base_action import BaseAction
from cqcli.infrastructure.base_option import BaseOption


class BaseCommand(ABC):
    name = ''
    help_doc = ''

    @property
    @abstractmethod
    def options(self) -> List[BaseOption]:
        pass

    @property
    @abstractmethod
    def actions(self) -> List[BaseAction]:
        pass

    def click_command(self) -> click.Command:
        def f(click_action, *args, **kwargs):
            for action in self.actions:
                if action.name == click_action:
                    ctx = click.get_current_context()
                    signature = inspect.signature(action.run)
                    params = {k: v for k, v in ctx.params.items() if k in signature.parameters}
                    action.run(**params)

        # 注册 argument
        action_argument = click.core.Argument(param_decls=('click_action',))
        click.decorators._param_memo(f, action_argument)

        for option in self.options:
            click_option = option.click_option()
            click.decorators._param_memo(f, click_option)

        context_settings = {
            'max_content_width': 500,
        }
        command = click.command(name=self.name, context_settings=context_settings)(f)
        return command
