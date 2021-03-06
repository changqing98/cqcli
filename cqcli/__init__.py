import logging

from . import config

version = '0.0.0'

# 设置 logging 的配置
level = logging._nameToLevel[config.LOG_LEVEL.upper()]
logging.basicConfig(
    level=level,
    format='%(levelname)-10s %(name)-10s %(message)s'
)
