from datetime import datetime
import json
import logging
import requests
import http.cookiejar as cj
import uuid

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
logging.basicConfig(level=logging.DEBUG,
                    format='{"asctime":"%(asctime)s","levelname":"%(levelname)s","message":"%(message)s"}',
                    datefmt='%Y-%m-%d %H:%M')  # 设置日志级别

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


class Store_info:

    def __init__(self):
        self.uuid = str(uuid.uuid4())
        self.Store_Host = Store_Host
        self.Store_Port = Store_Port
        self.Store_UserName = Store_UserName
        self.Store_Password = Store_Password
        self.deviceId = None
        self.login_status = 0
        self.headers = {'Content-Type': 'application/json'}
        self.r = requests.session()
        self.r.cookies = cj.LWPCookieJar()
        logging.info("巡检任务：" + self.uuid)
        self.login()
        if self.login_status == 1:
            self.system()
            self.controller()
            self.logout()

    def login(self):
        logging.info("存储地址：" + self.Store_Host)
        logging.info("存储端口：" + self.Store_Port)
        logging.info("存储用户：" + self.Store_UserName)
        url = "https://" + self.Store_Host + ":" + self.Store_Port + "/deviceManager/rest/xxxxx/sessions"
        logging.debug("登录URL：" + url)
        data = {"username": self.Store_UserName, "password": self.Store_Password, "scope": "0"}
        try:
            response = self.r.post(url, headers=self.headers, verify=False, data=json.dumps(data))
            logging.debug("登录返回：" + response.text)
            response = json.loads(response.text)
            if response["data"]["accountstate"] == 1:
                logging.info("登录成功")
                self.deviceId = response["data"]["deviceid"]
                iBaseToken = response["data"]["iBaseToken"]
                self.headers = {'Content-Type': 'application/json', "iBaseToken": iBaseToken}
                self.login_status = 1
                logging.info("设备ID：" + response["data"]["deviceid"])
                logging.info("登录用户：" + response["data"]["username"])
                logging.info("上次登录时间：" + str(datetime.fromtimestamp(response["data"]["lastlogintime"])))
                logging.info("上次登录IP：" + response["data"]["lastloginip"])
            else:
                logging.error("登录失败")
        except Exception:
            logging.error("系统异常")

    def system(self):
        logging.info("查询系统基本信息")
        url = "https://" + self.Store_Host + ":" + self.Store_Port + "/deviceManager/rest/" + self.deviceId + "/system/"
        logging.debug("调用URL：" + url)
        try:
            response = self.r.get(url, headers=self.headers, verify=False)
            logging.info("查询系统基本信息成功")
            info = json.loads(response.text)['data']
            logging.debug(info)
        except Exception:
            logging.error("系统异常")

    def controller(self):
        logging.info("查询控制器信息")
        url = "https://" + self.Store_Host + ":" + self.Store_Port + "/deviceManager/rest/" + self.deviceId + "/controller"
        logging.debug("调用URL：" + url)
        try:
            response = self.r.get(url, headers=self.headers, verify=False)
            logging.info("查询控制器信息成功")
            info = json.loads(response.text)['data']
            logging.debug(info)
        except Exception:
            logging.error("系统异常")

    def logout(self):
        url = "https://" + self.Store_Host + ":" + self.Store_Port + "/deviceManager/rest/" + self.deviceId + "/sessions"
        logging.debug("调用URL：" + url)
        try:
            self.r.delete(url, headers=self.headers, verify=False)
            logging.info("登出成功")
        except Exception:
            logging.error("系统异常")


if __name__ == '__main__':
    # logging.info("启动服务")
    # logging.info("数据采集间隔：" + str(SleepTime) + "秒")
    # logging.info("存储地址：" + Store_Host)
    # logging.info("存储端口：" + str(Store_Port))
    # logging.info("存储用户：" + Store_UserName)
    # try:
    #     logging.info("服务启动成功")
    #     while True:
    #         time.sleep(SleepTime)
    # except Exception as e:
    #     logging.error("服务异常")
    #     logging.error(e)
    Store_info()
