"""
在一个项目中,同等类型的工具,只使用一个
文件名: SendMethod.py
    1.参照项目接口文档进行编写
        请求地址
        请求方式:GET POST
        请求参数:
        - get请求带参数
            requests.get(url,params)
        - post请求带参数
            x-www-form-urlencoded格式
                requests.post(url,data)
            json格式
                requests.post(url,json)
        - post请求不带参数
            requests.post(url)
        返回值:
            - json格式: response.json()
"""
import csv

import paramiko
import requests
import datetime
import json

from Utils.Logger import logger


class SendMethod(object):
    @staticmethod
    def send_method(method, url, params=None, data=None, json=None, headers=None, complexjson=None):
        """
        封装请求
        :param method: 请求方式
        :param url: 请求地址
        :param params: get请求参数
        :param data: post请求参数,x-www-form-urlencoded格式
        :param json: post请求参数,json格式
        :return: result
        """
        if method == 'get':  # 请求方式为GET
            response = requests.get(url=url, params=params, headers=headers)
        elif method == 'post':  # 请求方式为POST
            if data is not None and json is None:  # 1.post请求 x-www-form-urlencoded格式
                response = requests.post(url=url, data=data, headers=headers)
            elif data is None and json is not None:  # 2.post请求 json格式
                response = requests.post(url=url, json=json, headers=headers)
            elif data is None and json is None:  # 3.post请求 不带参数
                response = requests.post(url=url, headers=headers)
            else:
                print('post请求参数类型错误')
                logger.info(f"【post请求参数类型错误】")
                response = None
        elif method == 'put':  # 请求方式为put
            if data is not None and json is None:  # 1.post请求 x-www-form-urlencoded格式
                response = requests.put(url=url, data=data, headers=headers)
            elif data is None and json is not None:  # 2.post请求 json格式
                response = requests.put(url=url, json=json, headers=headers)
            elif data is None and json is None:  # 3.post请求 不带参数
                response = requests.put(url=url, headers=headers)
            else:
                print('post请求参数类型错误')
                response = None
                logger.info(f"【post请求参数类型错误】")
        else:
            print('请求方式错误')
            response = None
        result = {}  # 响应结果
        if response is not None:
            result['status_code'] = response.status_code  # HTTP状态码
            try:
                result['body'] = response.json()  # 响应体 json格式
            except:
                result['body'] = response.text  # 响应体 text格式
            result['headers'] = response.headers  # 响应头
            result['response_time'] = int(response.elapsed.microseconds / 1000)  # 响应时间,以毫秒为单位
            a = response.request.url
            body = response.request.body
            logger.info(f"send==>>url:{a}  body: {body} 】")
            logger.info(f"response ==>>url:{a}  body: {result} 】")
            return result
        else:
            return None


if __name__ == '__main__':
    method = 'get'
    url = 'http://192.168.20.206/'
    payload = {'username': 'admin', 'password': 'macro123'}
    print(SendMethod.send_method(method=method, url=url, json=payload))
    a = input('输入ip:')
    b = input('输入账号:')
    # c = input('输入密码:')
    with paramiko.Transport(('118.114.172.171', 10022)) as trans:
        trans.connect(username='root', password='Enmo@2022_arm_kv101')
        ssh = paramiko.SSHClient()
        ssh._transport = trans
        while 1:
            command = input('输入指令:')
            if command == 'exit':
                break
            stdin, stdout, stderr = ssh.exec_command(command)
            print(stdout.read().decode())
            # print(stdin)
            print(stderr.read().decode())

# time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# print(time_stamp)
#
# print(time_stamp.strftime('%Y-%m-%d %H:%M:%S'))
