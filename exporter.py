import json

from prometheus_client import Gauge, Info


class exporter:
    def __init__(self):
        self.system_healthstatus = Gauge('system_healthstatus', '系统健康状态。参数取值：1：正常、2：故障', ["store_host"])
        self.system_runningstatus = Gauge('system_runningstatus', '系统运行状态。参数取值：1：正常、3：未运行、12：正在上电、47：正在下电、51：正在升级',
                                          ["store_host"])
        self.system_productversion = Info('system_productversion', '产品版本。', ["store_host"])
        self.system_patchversion = Info('system_patchversion', '补丁版本号。备注：当是补丁版本时返回此参数。', ["store_host"])
        self.system_memberdiskscapacity = Gauge('system_memberdiskscapacity', '所有加入硬盘域的成员盘裸容量之和。单位：sectors',
                                                ["store_host"])
        self.system_freediskscapacity = Gauge('system_freediskscapacity', '所有空闲盘裸容量之和，没有则为0。单位：sectors', ["store_host"])
        self.system_unavailablediskscapacity = Gauge('system_unavailablediskscapacity',
                                                     '所有不可用盘裸容量之和，没有则为0；不可用盘的定义为故障的成员盘和空闲盘，故系统总容量不算此容量。单位：sectors',
                                                     ["store_host"])
        self.system_storagepoolrawcapacity = Gauge('system_storagepoolrawcapacity', '所有存储池中盘总的裸容量。单位：sectors',
                                                   ["store_host"])
        self.system_storagepoolcapacity = Gauge('system_storagepoolcapacity', '所有存储池做完RAID后用户可用容量。单位：sectors',
                                                ["store_host"])
        self.system_storagepoolfreecapacity = Gauge('system_storagepoolfreecapacity', '所有存储池中还未分配的容量（RAID后）。单位：sectors',
                                                    ["store_host"])
        self.system_storagepoolhostsparecapacity = Gauge('system_storagepoolhostsparecapacity',
                                                         '所有存储池中预留的热备空间容量（RAID后）。单位：sectors', ["store_host"])
        self.system_sectorsize = Gauge('system_sectorsize', '扇区大小。单位：bytes', ["store_host"])

        self.system_totalcapacity = Gauge('system_totalcapacity', '系统总容量。单位：sectors', ["store_host"])
        self.system_usedcapacity = Gauge('system_usedcapacity', '系统已用容量。单位：sectors', ["store_host"])
        self.enclosure_healthstatus = Gauge('enclosure_healthstatus', '机框健康状态。参数取值：0：未知、1：正常、2：故障',
                                            ["store_host", "name"])
        self.enclosure_runningstatus = Gauge('enclosure_runningstatus', '运行状态。参数取值：0：未知、1：正常、2：运行、5：高温休眠、27：在线、28：离线',
                                             ["store_host", "name"])
        self.enclosure_model = Gauge('enclosure_model', '机框型号。详细取值范围请参考《华为存储RESTful API 接口参考》', ["store_host", "name"])
        self.enclosure_temperature = Gauge('enclosure_temperature', '温度。单位：℃', ["store_host", "name"])
        self.controller_healthstatus = Gauge('controller_healthstatus', '控制器健康状态。参数取值：0：未知、1：正常、2：故障、9：不一致',
                                             ["store_host", "location"])
        self.controller_runningstatus = Gauge('controller_runningstatus', '控制器运行状态。参数取值：0：未知、1：正常、2：运行、27：在线、28：离线',
                                              ["store_host", "location"])
        self.controller_memorysize = Gauge('controller_memorysize', 'Cache大小。单位：MB', ["store_host", "location"])
        self.controller_role = Gauge('controller_role', '控制器角色。参数取值：0：普通成员、1：集群主、2：集群备', ["store_host", "location"])
        self.controller_cpuusage = Gauge('controller_cpuusage', 'CPU占用率。', ["store_host", "location"])
        self.controller_memoryusage = Gauge('controller_memoryusage', '内存使用率。', ["store_host", "location"])
        self.controller_voltage = Gauge('controller_voltage', '控制器电压值。', ["store_host", "location"])
        self.controller_temperature = Gauge('controller_temperature', '温度。单位：°C', ["store_host", "location"])
        self.expboard_healthstatus = Gauge('expboard_healthstatus', '级联板健康状态。参数取值：0：未知、1：正常、2：故障',
                                           ["store_host", "location"])
        self.expboard_runningstatus = Gauge('expboard_runningstatus',
                                            '级联板运行状态。参数取值：0：未知、1：正常、2：运行、12：正在上电、13：已下电、27：在线、28：离线',
                                            ["store_host", "location"])
        self.intf_module_healthstatus = Gauge('intf_module_healthstatus', '接口模块健康状态。参数取值：0：未知、1：正常、2：故障',
                                              ["store_host", "location"])
        self.intf_module_runningstatus = Gauge('intf_module_runningstatus',
                                               '接口模块运行状态。参数取值：0：未知、1：正常、2：运行、12：正在上电、13：已下电、27：在线、28：离线、103：上电失败',
                                               ["store_host", "location"])
        self.intf_module_temperature = Gauge('intf_module_temperature', '温度。单位：°C', ["store_host", "location"])
        self.disk_healthstatus = Gauge('disk_healthstatus', '硬盘模块健康状态。参数取值：0：未知、1：正常、2：故障、3：即将故障',
                                       ["store_host", "location"])
        self.disk_runningstatus = Gauge('disk_runningstatus', '硬盘运行状态。参数取值：0：未知、1：正常、14：预拷贝、16：重构、27：在线、28：离线',
                                        ["store_host", "location"])
        self.disk_temperature = Gauge('disk_temperature', '硬盘温度。单位：°C', ["store_host", "location"])
        self.disk_disktype = Gauge('disk_disktype', '硬盘类型。详细取值范围请参考《华为存储RESTful API 接口参考》',
                                   ["store_host", "location"])
        self.disk_runtime = Gauge('disk_runtime', '硬盘运行天数。单位：day', ["store_host", "location"])
        self.disk_capacityusage = Gauge('disk_capacityusage', '硬盘容量利用率。单位：%', ["store_host", "location"])
        self.disk_healthmark = Gauge('disk_healthmark', '硬盘的健康评分。', ["store_host", "location"])
        self.disk_remainlife = Gauge('disk_remainlife', '硬盘剩余寿命。单位：days', ["store_host", "location"])
        self.power_healthstatus = Gauge('power_healthstatus', '电源模块健康状态。参数取值：0：未知、1：正常、2：故障、9：不一致、11：无输入',
                                        ["store_host", "location"])
        self.power_runningstatus = Gauge('power_runningstatus', '电源运行状态。参数取值：0：未知、1：正常、2：运行、27：在线、28：离线',
                                         ["store_host", "location"])
        self.power_temperature = Gauge('power_temperature', '电源温度。单位：°C', ["store_host", "location"])
        self.power_inputvoltage = Gauge('power_inputvoltage', '电源输入电压。单位：MV', ["store_host", "location"])
        self.power_outputvoltage = Gauge('power_outputvoltage', '电源输出电压。单位：MV', ["store_host", "location"])
        self.backup_power_healthstatus = Gauge('backup_power_healthstatus',
                                               '备电模块健康状态。参数取值：0：未知、1：正常、2：故障、3：即将故障、12：电量不足',
                                               ["store_host", "location"])
        self.backup_power_runningstatus = Gauge('backup_power_runningstatus',
                                                '备电模块运行状态。参数取值：0：未知、1：正常、2：运行、27：在线、28：离线、48：正在充电、49：充电完成、50：正在放电',
                                                ["store_host", "location"])
        self.backup_power_voltage = Gauge('backup_power_voltage', '当前电压，实际值为返回数据除以10。单位：V/10',
                                          ["store_host", "location"])
        self.backup_power_remainlifedays = Gauge('backup_power_remainlifedays', '剩余寿命。单位：days',
                                                 ["store_host", "location"])
        self.backup_power_chargetimes = Gauge('backup_power_chargetimes', '放电次数。', ["store_host", "location"])
        self.fan_healthstatus = Gauge('fan_healthstatus', '健康状态。参数取值：0：未知、1：正常、2：故障', ["store_host", "location"])
        self.fan_runningstatus = Gauge('fan_runningstatus', '运行状态。参数取值：0：未知、1：正常、2：运行、3：未运行、8：休眠、27：在线、28：离线',
                                       ["store_host", "location"])
        self.fan_runlevel = Gauge('fan_runlevel', '运行档位。参数取值：0：低、1：正常、2：高', ["store_host", "location"])

    def update(self, Store_Info):
        for name, data in Store_Info.items():
            store_host = data['store_host']
            self.system_healthstatus.labels(store_host=store_host).set(data["system"]["HEALTHSTATUS"])
            self.system_runningstatus.labels(store_host=store_host).set(data["system"]["RUNNINGSTATUS"])
            self.system_productversion.labels(store_host=store_host).info(
                {"productversion": data["system"]["PRODUCTVERSION"]})
            if "patchVersion" in data["system"]:
                self.system_patchversion.labels(store_host=store_host).info(
                    {"patchversion": data["system"]["patchVersion"]})
            else:
                self.system_patchversion.labels(store_host=store_host).info(
                    {"patchversion": ""})
            self.system_memberdiskscapacity.labels(store_host=store_host).set(data["system"]["MEMBERDISKSCAPACITY"])
            self.system_freediskscapacity.labels(store_host=store_host).set(data["system"]["FREEDISKSCAPACITY"])
            self.system_unavailablediskscapacity.labels(store_host=store_host).set(
                data["system"]["UNAVAILABLEDISKSCAPACITY"])
            self.system_storagepoolrawcapacity.labels(store_host=store_host).set(
                data["system"]["STORAGEPOOLRAWCAPACITY"])
            self.system_storagepoolcapacity.labels(store_host=store_host).set(data["system"]["STORAGEPOOLCAPACITY"])
            self.system_storagepoolfreecapacity.labels(store_host=store_host).set(
                data["system"]["STORAGEPOOLFREECAPACITY"])
            self.system_storagepoolhostsparecapacity.labels(store_host=store_host).set(
                data["system"]["STORAGEPOOLHOSTSPARECAPACITY"])
            self.system_sectorsize.labels(store_host=store_host).set(data["system"]["SECTORSIZE"])
            self.system_totalcapacity.labels(store_host=store_host).set(data["system"]["TOTALCAPACITY"])
            self.system_usedcapacity.labels(store_host=store_host).set(data["system"]["USEDCAPACITY"])
            for enclosure in data["enclosure"]:
                self.enclosure_healthstatus.labels(store_host=store_host, name=enclosure["NAME"]).set(
                    enclosure["HEALTHSTATUS"])
                self.enclosure_runningstatus.labels(store_host=store_host, name=enclosure["NAME"]).set(
                    enclosure["RUNNINGSTATUS"])
                self.enclosure_model.labels(store_host=store_host, name=enclosure["NAME"]).set(enclosure["MODEL"])
                self.enclosure_temperature.labels(store_host=store_host, name=enclosure["NAME"]).set(
                    enclosure["TEMPERATURE"])

            for controller in data["controller"]:
                self.controller_healthstatus.labels(store_host=store_host, location=controller["LOCATION"]).set(
                    controller["HEALTHSTATUS"])
                self.controller_runningstatus.labels(store_host=store_host, location=controller["LOCATION"]).set(
                    controller["RUNNINGSTATUS"])
                self.controller_memorysize.labels(store_host=store_host, location=controller["LOCATION"]).set(
                    controller["MEMORYSIZE"])
                self.controller_role.labels(store_host=store_host, location=controller["LOCATION"]).set(
                    controller["ROLE"])
                self.controller_cpuusage.labels(store_host=store_host, location=controller["LOCATION"]).set(
                    controller["CPUUSAGE"])
                self.controller_memoryusage.labels(store_host=store_host, location=controller["LOCATION"]).set(
                    controller["MEMORYUSAGE"])
                self.controller_voltage.labels(store_host=store_host, location=controller["LOCATION"]).set(
                    controller["VOLTAGE"])
                self.controller_temperature.labels(store_host=store_host, location=controller["LOCATION"]).set(
                    controller["TEMPERATURE"])
            for expboard in data["expboard"]:
                self.expboard_healthstatus.labels(store_host=store_host, location=expboard["LOCATION"]).set(
                    expboard["HEALTHSTATUS"])
                self.expboard_runningstatus.labels(store_host=store_host, location=expboard["LOCATION"]).set(
                    expboard["RUNNINGSTATUS"])
            for intf_module in data["intf_module"]:
                self.intf_module_healthstatus.labels(store_host=store_host, location=intf_module["LOCATION"]).set(
                    intf_module["HEALTHSTATUS"])
                self.intf_module_runningstatus.labels(store_host=store_host, location=intf_module["LOCATION"]).set(
                    intf_module["RUNNINGSTATUS"])
                self.intf_module_temperature.labels(store_host=store_host, location=intf_module["LOCATION"]).set(
                    intf_module["TEMPERATURE"])
            for disk in data["disk"]:
                self.disk_healthstatus.labels(store_host=store_host, location=disk["LOCATION"]).set(
                    disk["HEALTHSTATUS"])
                self.disk_runningstatus.labels(store_host=store_host, location=disk["LOCATION"]).set(
                    disk["RUNNINGSTATUS"])
                self.disk_temperature.labels(store_host=store_host, location=disk["LOCATION"]).set(disk["TEMPERATURE"])
                self.disk_disktype.labels(store_host=store_host, location=disk["LOCATION"]).set(disk["DISKTYPE"])
                self.disk_runtime.labels(store_host=store_host, location=disk["LOCATION"]).set(disk["RUNTIME"])
                self.disk_healthmark.labels(store_host=store_host, location=disk["LOCATION"]).set(disk["HEALTHMARK"])
                self.disk_remainlife.labels(store_host=store_host, location=disk["LOCATION"]).set(disk["REMAINLIFE"])
            for power in data["power"]:
                self.power_healthstatus.labels(store_host=store_host, location=power["LOCATION"]).set(
                    power["HEALTHSTATUS"])
                self.power_runningstatus.labels(store_host=store_host, location=power["LOCATION"]).set(
                    power["RUNNINGSTATUS"])
                self.power_temperature.labels(store_host=store_host, location=power["LOCATION"]).set(
                    power["TEMPERATURE"])
                self.power_inputvoltage.labels(store_host=store_host, location=power["LOCATION"]).set(
                    power["INPUTVOLTAGE"])
                self.power_outputvoltage.labels(store_host=store_host, location=power["LOCATION"]).set(
                    power["OUTPUTVOLTAGE"])
            for backup_power in data["backup_power"]:
                self.backup_power_healthstatus.labels(store_host=store_host, location=backup_power["LOCATION"]).set(
                    backup_power["HEALTHSTATUS"])
                self.backup_power_runningstatus.labels(store_host=store_host, location=backup_power["LOCATION"]).set(
                    backup_power["RUNNINGSTATUS"])
                self.backup_power_voltage.labels(store_host=store_host, location=backup_power["LOCATION"]).set(
                    backup_power["VOLTAGE"])
                self.backup_power_remainlifedays.labels(store_host=store_host, location=backup_power["LOCATION"]).set(
                    backup_power["REMAINLIFEDAYS"])
                self.backup_power_chargetimes.labels(store_host=store_host, location=backup_power["LOCATION"]).set(
                    backup_power["CHARGETIMES"])
            for fan in data["fan"]:
                self.fan_healthstatus.labels(store_host=store_host, location=fan["LOCATION"]).set(fan["HEALTHSTATUS"])
                self.fan_runningstatus.labels(store_host=store_host, location=fan["LOCATION"]).set(fan["RUNNINGSTATUS"])
                self.fan_runlevel.labels(store_host=store_host, location=fan["LOCATION"]).set(fan["RUNLEVEL"])

            print(store_host)
