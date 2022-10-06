from datetime import datetime

from prometheus_client import Gauge
from prometheus_client import start_http_server
from prometheus_client import Info


class exporter:
    def __init__(self):
        self.system_sectorsize = Gauge('system_sectorsize', '扇区大小。单位：bytes', ["store_host"])
        self.system_memberdiskscapacity = Gauge('system_memberdiskscapacity', '所有加入硬盘域的成员盘裸容量之和。单位：sectors',
                                                ["store_host"])
        self.system_totalcapacity = Gauge('system_totalcapacity', '系统总容量。单位：sectors', ["store_host"])

    def update(self, Store_Info):
        for name, data in Store_Info.items():
            store_host = data['store_host']
            self.system_sectorsize.labels(store_host=store_host).set(data["system"]["SECTORSIZE"])
            self.system_memberdiskscapacity.labels(store_host=store_host).set(data["system"]["MEMBERDISKSCAPACITY"])
            self.system_totalcapacity.labels(store_host=store_host).set(data["system"]["TOTALCAPACITY"])
            print(store_host)
