import time
import random
from prometheus_client import start_http_server, Gauge
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='{"asctime":"%(asctime)s","levelname":"%(levelname)s","message":"%(message)s"}',
                    datefmt='%Y-%m-%d %H:%M')  # 设置日志级别

# 数据采集间隔，单位秒
SleepTime = 10
# 启动端口
Port = 8000
# 存储地址
Store_Host = "10.1.1.1"
# 存储端口
Store_Port = 8088
# 用户名
Store_UserName = "admin"
Store_Password = "admin"

Storage_login_status = Gauge('Storage_login_status', 'Description of gauge', ['Store_Host'])


class Store_info:
    def __int__(self):
        self.login_status()

    # 登录状态检测
    def login_status(self):
        logging.DEBUG("登录状态检测")
        Storage_login_status.labels(Store_Host=Store_Host).set(1)


if __name__ == '__main__':
    logging.info("启动服务")
    logging.info("服务端口：" + str(Port))
    logging.info("数据采集间隔：" + str(SleepTime) + "秒")
    logging.info("存储地址：" + Store_Host)
    logging.info("存储端口：" + str(Store_Port))
    logging.info("存储用户：" + Store_UserName)
    try:
        start_http_server(Port)
        logging.info("服务启动成功")
        while True:
            time.sleep(SleepTime)
            Storage_login_status.labels(Store_Host=Store_Host).set(1)  # 本机IP传入labels，CPU使用率传入value
    except Exception as e:
        logging.error("服务异常")
        logging.error(e)
