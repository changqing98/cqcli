# 项目所有的配置信息在这里定义
import os

# 配置文件路径
CONFIG_DIR = os.environ.get('CQCLI_CONFIG_DIR', os.path.expanduser('~/.config/cqcli'))
CONFILE_FILE_PATH = os.environ.get(
    'CQCLI_CONFIG_PATH', os.path.join(CONFIG_DIR, 'config.ini')
)

WORK_DIR = os.environ.get('CQCLI_WORK_DIR', os.path.abspath('/tmp/cqcli'))

# 默认日志级别
LOG_LEVEL = os.environ.get('CQCLI_LOG_LEVEL', 'INFO')
