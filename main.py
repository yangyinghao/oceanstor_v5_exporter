import _thread
import configparser
import json
import time
import logging
from OceanStor import Store

oceanstor = configparser.ConfigParser()
oceanstor.read("oceanstor.ini")
base = configparser.ConfigParser()
base.read("base.ini")
oceanstors = oceanstor.sections()

logging.basicConfig(level=logging.DEBUG,
                    format='{"asctime":"%(asctime)s","levelname":"%(levelname)s","message":"%(message)s"}',
                    datefmt='%Y-%m-%d %H:%M:%S')  # 设置日志级别

# 数据采集间隔，单位秒
SleepTime = int(base.get("monitor", "sleeptime"))
# 启动端口
Port = base.get("service", "port")
# 存储地址

Store_Info = {}


def get_store_info():
    global Store_Info
    global store
    global SleepTime
    while True:
        for store in oceanstors:
            logging.info(store + "开始巡检")
            Store_Info[store] = Store(oceanstor.get(store, "Store_Host"), oceanstor.get(store, "Store_Port"),
                                      oceanstor.get(store, "Store_UserName"),
                                      oceanstor.get(store, "Store_Password")).get_store_info()
            logging.info(store + "巡检结束")

        time.sleep(SleepTime)


def exporter():
    global Store_Info
    while True:
        print(json.dumps(Store_Info))
        # print(Store_Info)
        time.sleep(1)


if __name__ == '__main__':
    for store in oceanstors:
        logging.info(store + "开始巡检")
        Store_Info[store] = Store(oceanstor.get(store, "Store_Host"), oceanstor.get(store, "Store_Port"),
                                  oceanstor.get(store, "Store_UserName"),
                                  oceanstor.get(store, "Store_Password")).get_store_info()
        logging.info(store + "巡检结束")

    print(Store_Info)
    try:
        _thread.start_new_thread(get_store_info, ())
        _thread.start_new_thread(exporter, ())
    except Exception as e:
        logging.error("无法启动线程")
        logging.error(e)
    while True:
        pass
