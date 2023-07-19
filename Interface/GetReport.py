# -*- coding: utf-8 -*-
import csv
import random
import re

from Utils.GetKeyword import GetKeyword
from Utils.SendMethod import SendMethod
from Utils.Database import Database
from Utils.OperationConfig import OperationConfig
import json
import concurrent.futures
from datetime import datetime, timedelta
import time


class GetReport(object):
    def __init__(self):
        config = OperationConfig()
        self.url = config.get_option('test', 'url')
        self.headers = json.loads(config.get_option('test', 'headers'))

    def get_report(self):
        """得到错题"""
        method = 'get'
        url = 'https://www.iq-test.top/direct/psyc/download/pdf/290548/1/zh-CN'
        return SendMethod.send_method(method=method, url=url)


if __name__ == '__main__':
    # lists = [0, 1, 2, 3]
    import requests


    def task(x):
        for id in x:
            url = f"https://www.iq-test.top/direct/psyc/download/pdf/{id}/1/zh-CN"  # 文件的URL
            print(id)
            print(url)
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    with open(f"{id}.pdf", "wb") as file:
                        file.write(response.content)
                    print(f"文件{id}保存成功")
                else:
                    print("文件下载失败")
            except Exception as e:
                print("不存在pdf", str(e))
    file_path = "无标题.csv"  # CSV文件路径

    with open(file_path, "r", newline="") as file:
        reader = csv.reader(file)
        with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
            # 提交任务到线程池
            # futures = [executor.submit(task) for row in reader]
            futures = [executor.submit(lambda x: task(x), row) for row in reader]
            print(f"Task number:", len(futures))
            for future in concurrent.futures.as_completed(futures):
                try:
                    result = future.result()
                    print(f"Task result: {result}")
                except Exception as e:
                    print(f"Task encountered an exception: {e}")

    # lists = []
    # for i in lists:
    #     url = f"https://www.iq-test.top/direct/psyc/download/pdf/{id}/1/zh-CN"  # 文件的URL
    #     response = requests.get(url)
    #
    #     if response.status_code == 200:
    #         with open("downloaded_file.pdf", "wb") as file:
    #             file.write(response.content)
    #         print("文件保存成功")
    #     else:
    #         print("文件下载失败")
#     def task():
#         # respons = GetReport().get_report()
#         dicts = {}
#         respons = '''
# <html>
# <body>
# <a href="https://www.example.com">Example Website</a>
# </body>
# </html>
# '''
#         pattern = r'<a\s+href="(.*?)">'
#         html1 = re.findall(pattern, respons)
#         dicts['abc'] = 1
#         dicts['abcd'] = 123
#         print(dicts)
#
#         # pattern = r''
#         # html2 = re.findall(pattern, respons)
#         # dicts['abc'] = html2
#         #
#         # pattern = r''
#         # html2 = re.findall(pattern, respons)
#         # dicts['abc'] = html2
#         #
#         # pattern = r''
#         # html2 = re.findall(pattern, respons)
#         # dicts['abc'] = html2
#         #
#         # pattern = r''
#         # html2 = re.findall(pattern, respons)
#         # dicts['abc'] = html2
#         #
#         # pattern = r''
#         # html2 = re.findall(pattern, respons)
#         # dicts['abc'] = html2
#         #
#         # pattern = r''
#         # html2 = re.findall(pattern, respons)
#         # dicts['abc'] = html2
#
#         csv_file = 'data.csv'
#         with open(csv_file, 'a', newline='') as file:
#             # writer = csv.writer(file)
#             # writer.writerows(str(dicts))
#             json.dump(dicts, file)
#             file.write('\n')
#
#
#     with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
#         # 提交任务到线程池
#         futures = [executor.submit(task) for i in lists]
#         print(f"Task number:", len(futures))
#         for future in concurrent.futures.as_completed(futures):
#             try:
#                 result = future.result()
#                 print(f"Task result: {result}")
#             except Exception as e:
#                 print(f"Task encountered an exception: {e}")
