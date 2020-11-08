from cqcli.infrastructure.base_option import BaseOption

output_path = BaseOption(
    param=('-o', '--output'),
    help="输出路径",
    default='./'
)

language = BaseOption(
    param=('-l', '--language'),
    help="输出语言"
)

version = BaseOption(
    param=('-v', '--version'),
    help="版本",
    default="1.0.0"
)
ALL = [output_path, version]
