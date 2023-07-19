"""
模块名称: 登录模块
    模块中的每一个接口至少写一个方法,当接口存在关联时,还需要写对应接口的关联方法
    - 接口录入
    - 接口关联
"""
import csv
import random

import paramiko

from Utils.SendMethod import SendMethod
from Utils.GetKeyword import GetKeyword
from Utils.OperationConfig import OperationConfig
from Utils.Database import Database
import pandas
import json


class LogInInterface(object):
    def __init__(self):
        self.config = OperationConfig()
        self.url = self.config.get_option('test', 'url')

    def member_login(self):
        """登录"""
        method = 'get'  # 请求参数类型 x-www-form-urlencoded格式
        url = self.url + '/dbaasApiGateWay/doLogin'
        payload = {'username': 'supertest', 'password': 'qF3IxNmEOPOnxYLMnCMrFg=='}
        return SendMethod.send_method(method=method, url=url, params=payload)

    def member_logout(self):
        method = 'get'  # 请求参数类型 x-www-form-urlencoded格式
        url = self.url + '/dbaasApiGateWay/logout'
        return SendMethod.send_method(method=method, url=url)

    def model_load(self):
        method = 'get'
        # result = self.member_login()
        # headers=GetKeyword.get_keyword(result, 'headers')
        headers = self.config.get_option('test', 'headers')
        headers = json.loads(headers)
        # headers = {"Cookie": "SESSION=c2bd9bee-a369-41ad-847c-7efc387db15b"}
        # print(headers,type(headers))

        # url = 'http://192.168.20.115/dbaasDbManage/paramGroup/paramAvailable?paramJson=%7B%22dbType%22:%22MySQL%22,%22dbVersion%22:%2210.2%22%7D'
        url = 'http://192.168.20.115/dbaasDbManage/paramGroup/paramAvailable?lang=zh_CN&t=1650953126708&paramJson=%7B%22dbType%22:%22MySQL%22,%22dbVersion%22:%228.0%22%7D'
        payload = {'dbServiceId': '1650423242502', 'variableName': 'd262da84f09d41d3bbff138d8fd38992',
                   't': 1650423242502}
        return SendMethod.send_method(method=method, url=url, params=payload, headers=headers)

    def model_update(self, variableName, newValue):
        method = 'post'
        headers = self.config.get_option('test', 'headers')
        headers = json.loads(headers)
        url = 'http://192.168.20.115/dbaasMariadb/config/variable/update'
        payload = {
            "dbServiceId": "b75888716cf3474a9ac3647588329c5c",
            "variableName": f"{variableName}",
            "oldValue": "",
            "newValue": f"{newValue}",
            "itemDynamic": 0
        }
        return SendMethod.send_method(method=method, url=url, json=payload, headers=headers)

    def get_member_token(self):
        """
        获取session
        :return:
        """
        result = self.member_login()
        # print(result)
        a = GetKeyword.get_keyword(result, 'headers')
        Cookie = a.get('Set-Cookie').split(';')[0]
        headers = {'Cookie': f'{Cookie}'}
        # print(headers)
        self.config.set_option('test', 'headers', json.dumps(headers))

    def data_anxin(self):
        """
        对接接口
        :return:
        """
        method = 'get'
        headers = self.config.get_option('test', 'headers')
        headers = json.loads(headers)
        url = 'http://192.168.20.115:80/essenceSecurities/mysql/api/user/create'
        payload = {
            "clusterId": "bc342b8a67084346b7c316da3c0fed5d",
            "userName": "jtq_new",
            "pwd": "123123..",
            "isExpire": "true",
            "host": "%",
            "workPlatformId": "workOrderId-2",
            "globalPrivateList": ["Select"],
            "mysqlSchemaList": [{
                "schemaName": "autoDB",
                "charset": "utf8mb4",
                "sortRule": "utf8mb4_general_ci",
                "privateList": ["select", "delete"],
                "tableList": [{
                    "table": "tb_user",
                    "privateList": ["select"]
                }]
            }],

            "workPlatformName": "测试工单创建用户",
            "callBackServiceUrl": "http://www.baidu.com",
            "envType": "dev",
            "workOrderId": "workOrderId"
        }
        return SendMethod.send_method(method=method, url=url, params=payload, headers=headers)


if __name__ == '__main__':
    # login = LogInInterface()
    # # # print(login.data_get())
    # # # print(login.member_login())
    # login.get_member_token()
    # # # print(login.model_update())
    # result = login.model_load()
    # # print(result)
    #
    # list0 = GetKeyword.get_keywords(result, 'itemName')
    # list1 = list(set(list0))
    # print(f"接口的元素元素个数:{len(list0)}")
    # print(f"接口的元素去重后个数:{len(list1)}")
    #
    # #登录数据库,执行sql
    # db = Database()
    # sql = '''select item_name from dbaas.db_param_item where db_type='mysql' and db_version=8.0;'''
    # result_sql = db.readall(sql=sql)
    # list_db = [i.get("item_name") for i in result_sql]
    # list_db = list(set(list_db))
    # print(f"数据库10.2的元素个数:{len(result_sql)}")
    # print(f"数据库10.2的元素去重后个数:{len(list_db)}")
    #
    # # 相同元素
    # a = [x for x in list1 if x in list_db]
    # # 两个列表中的不同元素
    # b = [y for y in (list1 + list_db) if y not in a]
    # print(f"相同元素个数:{len(a)}")
    # print(f"不相同元素个数:{len(b)},元素是:{b}")
    #
    # #重复元素
    # for j in b:
    #     print(list_db.count(j), j)
    # d = {}
    # for s in list1:
    #     count = 0
    #     for i in list0:
    #         if i == s:
    #             count += 1
    #             d[s] = count
    # for k, v in d.items():
    #     if v > 1:
    #         print("元素{}, 重复{}次".format(k, v))
    #
    # # 构造传入不定长的参数
    # input_model_in = ""
    # for i in range(1, 10):
    #     input_model = random.sample(list0, i)
    #     for j in input_model:
    #         input_model_in = input_model_in + j
    #
    # for input_model_in in list1:
    #     # 请求修改接口,传入修改值和原始值
    #     result_update = login.model_update(variableName=input_model_in, newValue=input_model_in)
    #     if GetKeyword.get_keywords(result_update, 'msg') == '操作失败':
    #         print(f"参数{input_model_in}设置失败")
    #
    # print(login.model_update(variableName='skip-name-resolve', newValue='skip-name-resolve'))
    # print(GetKeyword.get_keywords(login.model_update(variableName='skip-name-resolve', newValue='skip-name-resolve'), 'msg'))
    # list_fail = [input_model_in for input_model_in in list1 if GetKeyword.get_keywords(login.model_update(variableName='skip-name-resolve', newValue=input_model_in), 'msg') != ['参数修改成功']]
    # print(list_fail)
    # # 连接主机,查询mysql参数,查询重启生效的参数
    # with paramiko.Transport(('192.168.90.31', 22)) as trans:
    #     trans.connect(username='root', password='root123')
    #     ssh = paramiko.SSHClient()
    #     ssh._transport = trans
    #     stdin, stdout, stderr = ssh.exec_command('cat /etc/my.cnf')
    #     my_cnf = stdout.read().decode()
    #     # print(type(my_cnf),my_cnf)
    #     print(my_cnf)
    # #     if my_cnf.find('pid-file') != -1 and my_cnf.find('old-file') == -1:
    # #         print('参数创建成功')
    # #     else:
    # #         print('未找到配置参数,原参数:{old-file},新参数:{}')
    # # print(512*1024*1024*1024)
    # # print(login.data_anxin())
    # # print(int("21")>"3")
    # db = Database()
    # sql = '''select item_name,item_value_available from dbaas.db_param_item where db_type='mysql' and item_value_type='string' ;'''
    #
    # result_sql = db.readall(sql=sql)
    # for i in result_sql:
    #     # print(i)
    #     if i.get('item_value_available') != '' and ("," not in i.get('item_value_available')) and float(
    #             i.get('item_value_available').split('-')[-1]) > (2 ** 53):
    #         # print(i.get('item_value_available').split('-')[-1])
    #         # a = float(i.get('item_value_available').split('-')[-1])
    #         # if a>(2**53):
    #         a = i.get('item_value_available')
    #         b = i.get('item_name')
    #         print(a, b)

        # try:
        #     if int(i.get('item_value_available').split('-')[-1]):
        #         a = i.get('item_name')
        #         b = i.get("item_value_available")
        #         print(a, b)
        # finally:
        #     print(1)
    # print(result_sql)
    import requests



    file_path = "无标题.csv"  # CSV文件路径

    with open(file_path, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[0])
        # with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        #     # 提交任务到线程池
        #     # futures = [executor.submit(task) for row in reader]
        #     futures = [executor.submit(lambda x: task(x), row[0]) for row in reader]
        #     print(f"Task number:", len(futures))
        #     for future in concurrent.futures.as_completed(futures):
        #         try:
        #             result = future.result()
        #             print(f"Task result: {result}")
        #         except Exception as e:
        #             print(f"Task encountered an exception: {e}")
