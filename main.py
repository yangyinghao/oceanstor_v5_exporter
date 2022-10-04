import _thread
import time
import logging
from OceanStor import Store

logging.basicConfig(level=logging.DEBUG,
                    format='{"asctime":"%(asctime)s","levelname":"%(levelname)s","message":"%(message)s"}',
                    datefmt='%Y-%m-%d %H:%M:%S')  # 设置日志级别

# 数据采集间隔，单位秒
SleepTime = 10
# 启动端口
Port = 8000
# 存储地址
Store_Host = "192.168.32.99"
# 存储端口
Store_Port = "8088"
# 用户名
Store_UserName = "monitor"
Store_Password = "1qazXSW@3edc"

Store_Info = None


def get_store_info():
    global Store_Info
    while True:
        Store_Info = Store(Store_Host, Store_Port, Store_UserName, Store_Password).get_store_info()
        time.sleep(30)


def exporter():
    global Store_Info
    while True:
        print(Store_Info)
        time.sleep(1)


if __name__ == '__main__':
    Store_Info = Store(Store_Host, Store_Port, Store_UserName, Store_Password).get_store_info()
    # print(Store_Info)
    # try:
    #     _thread.start_new_thread(get_store_info, ())
    #     _thread.start_new_thread(exporter, ())
    # except:
    #     print("Error: 无法启动线程")
    #
    # while 1:
    #     pass
