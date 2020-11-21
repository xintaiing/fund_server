SETTINGS_DEBUG = False

if SETTINGS_DEBUG:
    # 日志名
    LOGGER_NAME = "dev"
    LOCAL_HOST = "139.196.212.119"
    pass
else:
    # 日志名
    LOGGER_NAME = "product"
    LOCAL_HOST = "172.28.2.72"

# db conn config
DB_NAME = "fund_server"
DB_USER = "root"
DB_PASSWORD = "FS.2020.11.11.sxt"
DB_HOST = LOCAL_HOST
DB_PORT = "3306"

REDIS_HOST = LOCAL_HOST
REDIS_PORT = "6379"
