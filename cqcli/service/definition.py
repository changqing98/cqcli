class Service:
    name = ''
    display_name = ''
    description = ''

    @classmethod
    def help_msg(cls) -> str:
        return ''

    @classmethod
    def config_template(cls) -> str:
        return ''