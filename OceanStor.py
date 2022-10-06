from datetime import datetime
import json
import logging
import requests
import http.cookiejar as cj
import uuid
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Store:

    def __init__(self, store_host, store_port, store_userName, store_password):
        self.Store_Info = None
        self.uuid = str(uuid.uuid4())
        self.Store_Host = store_host
        self.Store_Port = store_port
        self.Store_UserName = store_userName
        self.Store_Password = store_password
        self.deviceId = None
        self.login_status = 0
        self.headers = {'Content-Type': 'application/json'}
        self.r = requests.session()
        self.r.cookies = cj.LWPCookieJar()
        logging.info("巡检任务：" + self.uuid)

    def get_store_info(self):
        self.login()
        if self.login_status == 1:
            system = self.system()
            controller = self.controller()
            expboard = self.expboard()
            intf_module = self.intf_module()
            disk = self.disk()
            power = self.power()
            backup_power = self.backup_power()
            fan = self.fan()
            self.logout()
            self.Store_Info = {"store_host": self.Store_Host, "updatetime": int(datetime.now().timestamp()),
                               "system": system, "controller": controller, "expboard": expboard,
                               "intf_module": intf_module, "disk": disk, "power": power, "backup_power": backup_power,
                               "fan": fan}
            logging.debug(self.Store_Info)

        return self.Store_Info

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
            if response["error"]["code"] == 0:
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
                logging.error("登录失败,失败原因：" + str(response["error"]))
        except Exception as e:
            logging.error("系统异常")
            logging.error(e)

    def system(self):
        logging.info("查询系统基本信息")
        url = "https://" + self.Store_Host + ":" + self.Store_Port + "/deviceManager/rest/" + self.deviceId + "/system/"
        logging.debug("调用URL：" + url)
        try:
            response = self.r.get(url, headers=self.headers, verify=False)
            logging.info("查询系统基本信息成功")
            info = json.loads(response.text)["data"]
            logging.debug(response.text)
            return info
        except Exception as e:
            logging.error("系统异常")
            logging.error(e)
            return "Error"

    def controller(self):
        logging.info("查询控制器信息")
        url = "https://" + self.Store_Host + ":" + self.Store_Port + "/deviceManager/rest/" + self.deviceId + "/controller"
        logging.debug("调用URL：" + url)
        try:
            response = self.r.get(url, headers=self.headers, verify=False)
            logging.info("查询控制器信息成功")
            info = json.loads(response.text)['data']
            logging.debug(response.text)
            return info
        except Exception as e:
            logging.error("系统异常")
            logging.error(e)
            return "Error"

    def expboard(self):
        logging.info("查询级联板信息")
        url = "https://" + self.Store_Host + ":" + self.Store_Port + "/deviceManager/rest/" + self.deviceId + "/expboard"
        logging.debug("调用URL：" + url)
        try:
            response = self.r.get(url, headers=self.headers, verify=False)
            logging.info("查询级联板信息成功")
            info = json.loads(response.text)['data']
            logging.debug(response.text)
            return info
        except Exception as e:
            logging.error("系统异常")
            logging.error(e)
            return "Error"

    def intf_module(self):
        logging.info("查询接口模块信息")
        url = "https://" + self.Store_Host + ":" + self.Store_Port + "/deviceManager/rest/" + self.deviceId + "/intf_module"
        logging.debug("调用URL：" + url)
        try:
            response = self.r.get(url, headers=self.headers, verify=False)
            logging.info("查询接口模块信息成功")
            info = json.loads(response.text)['data']
            logging.debug(response.text)
            return info
        except Exception as e:
            logging.error("系统异常")
            logging.error(e)
            return "Error"

    def disk(self):
        logging.info("查询硬盘的基本信息")
        url = "https://" + self.Store_Host + ":" + self.Store_Port + "/deviceManager/rest/" + self.deviceId + "/disk"
        logging.debug("调用URL：" + url)
        try:
            response = self.r.get(url, headers=self.headers, verify=False)
            logging.info("查询硬盘的基本信息成功")
            info = json.loads(response.text)['data']
            logging.debug(response.text)
            return info
        except Exception as e:
            logging.error("系统异常")
            logging.error(e)
            return "Error"

    def power(self):
        logging.info("查询电源的基本信息")
        url = "https://" + self.Store_Host + ":" + self.Store_Port + "/deviceManager/rest/" + self.deviceId + "/power"
        logging.debug("调用URL：" + url)
        try:
            response = self.r.get(url, headers=self.headers, verify=False)
            logging.info("查询电源的基本信息成功")
            info = json.loads(response.text)['data']
            logging.debug(response.text)
            return info
        except Exception as e:
            logging.error("系统异常")
            logging.error(e)
            return "Error"

    def backup_power(self):
        logging.info("查询备电模块的基本信息")
        url = "https://" + self.Store_Host + ":" + self.Store_Port + "/deviceManager/rest/" + self.deviceId + "/backup_power"
        logging.debug("调用URL：" + url)
        try:
            response = self.r.get(url, headers=self.headers, verify=False)
            logging.info("查询备电模块的基本信息成功")
            info = json.loads(response.text)['data']
            logging.debug(response.text)
            return info
        except Exception as e:
            logging.error("系统异常")
            logging.error(e)
            return "Error"

    def fan(self):
        logging.info("查询风扇的基本信息")
        url = "https://" + self.Store_Host + ":" + self.Store_Port + "/deviceManager/rest/" + self.deviceId + "/fan"
        logging.debug("调用URL：" + url)
        try:
            response = self.r.get(url, headers=self.headers, verify=False)
            logging.info("查询风扇的基本信息成功")
            info = json.loads(response.text)['data']
            logging.debug(response.text)
            return info
        except Exception as e:
            logging.error("系统异常")
            logging.error(e)
            return "Error"

    def logout(self):
        url = "https://" + self.Store_Host + ":" + self.Store_Port + "/deviceManager/rest/" + self.deviceId + "/sessions"
        logging.debug("调用URL：" + url)
        try:
            self.r.delete(url, headers=self.headers, verify=False)
            logging.info("登出成功")
        except Exception as e:
            logging.error("系统异常")
            logging.error(e)
