import click

name = click.Option(
    param_decls=('-n', '--name'),
    help="姓名",
    default='cqcli'
)

ALL = [name]
