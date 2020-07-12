import click

output_path = click.Option(
    param_decls=('-o', '--output'),
    help="输出路径",
    default='./'
)

ALL = [output_path]
