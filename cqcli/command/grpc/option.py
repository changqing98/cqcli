import click

output_path = click.Option(
    param_decls=('-o', '--output'),
    help="输出路径",
    default='./'
)

language = click.Option(
    param_decls=('-l', '--language'),
    help="输出语言"
)

ALL = [output_path]
