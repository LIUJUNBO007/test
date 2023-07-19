# -*- coding: utf-8 -*-
import random

from Utils.GetKeyword import GetKeyword
from Utils.SendMethod import SendMethod
from Utils.Database import Database
from Utils.OperationConfig import OperationConfig
import json
import concurrent.futures
from datetime import datetime, timedelta
import time


class AddressInterface(object):
    def __init__(self):
        config = OperationConfig()
        self.url = config.get_option('test', 'url')
        self.headers = json.loads(config.get_option('test', 'headers'))

    def en_face(self):
        "首页"
        method = 'get'
        url = self.url + '/en'
        return SendMethod.send_method(method=method, url=url)

    def task(self, name):
        print(f"Task {name} started")
        # 执行任务的具体操作，这里只是简单地模拟耗时操作
        result = sum(range(1, 10000000))
        print(f"Task {name} finished")
        return result

    def search_conutry_list(self):
        method = 'post'
        url = self.url + '/taotan_admin_api/region/list'
        payload = {}
        return SendMethod.send_method(method=method, url=url, headers=self.headers, json=payload)

    def add_conutry_list(self):
        method = 'post'
        url = self.url + '/taotan_admin_api/region/save'
        payload = {"name": "sss1"}
        return SendMethod.send_method(method=method, url=url, headers=self.headers, json=payload)

    def mail_mode(self, payload):
        method = 'post'
        url = self.url + '/taotan_admin_api/email/config/edit'
        return SendMethod.send_method(method=method, url=url, headers=self.headers, json=payload)

    def question_sub(self, payload):
        method = 'post'
        url = self.url + '/api/exam/order/info'
        return SendMethod.send_method(method=method, url=url, json=payload)


if __name__ == '__main__':
    # en_face = AddressInterface()
    # with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
    # 提交任务到线程池
    # futures = [executor.submit(en_face.mail_mode, payload={
    #     "id": i,
    #     "name": f"aaaaaaAAAAcesCE测试ａａａ{i}",
    #     "address": "test",
    #     "port": "121",
    #     "account": "aaaaaaaaaaaa",
    #     "password": " 15",
    #     "fromAddress": "www.baidu.com",
    #     "replyToAddress": "www.baidu.com",
    #     "ctime": "2023-06-20 09:27:59",
    #     "utime": "2023-06-20 10:03:14",
    #     "status": 1
    # }) for i in range(200, 400)]
    # print(f"Task number:", len(futures))
    # for future in concurrent.futures.as_completed(futures):
    #     try:
    #         result = future.result()
    #         print("Task time:", GetKeyword.get_keywords(source=result, keyword='response_time')[-1])
    #         print(f"Task result: {result}")
    #     except Exception as e:
    #         print(f"Task encountered an exception: {e}")
    en_face = AddressInterface()
    current_time = datetime.now()

    # 偏移5分钟
    offset = timedelta(minutes=5)
    new_time = current_time - offset
    # 将新时间格式化为字符串
    new_time_str = new_time.strftime("%Y-%m-%dT%H:%M:%S")
    current_time_str = current_time.strftime("%Y-%m-%dT%H:%M:%S")
    payload = {
        "appExamId": "1511",
        "examId": "IIQQ",
        "endTime": f"{current_time_str}",
        "startTime": f"{new_time_str}",
        "questions": [
            {
                "examAnswerIds": [
                    959296
                ],
                "examQuestionId": 219583
            },
            {
                "examAnswerIds": [
                    959230
                ],
                "examQuestionId": 219572
            },
            {
                "examAnswerIds": [
                    959236
                ],
                "examQuestionId": 219573
            },
            {
                "examAnswerIds": [
                    959242
                ],
                "examQuestionId": 219574
            },
            {
                "examAnswerIds": [
                    959248
                ],
                "examQuestionId": 219575
            },
            {
                "examAnswerIds": [
                    959254
                ],
                "examQuestionId": 219576
            },
            {
                "examAnswerIds": [
                    959260
                ],
                "examQuestionId": 219577
            },
            {
                "examAnswerIds": [
                    959266
                ],
                "examQuestionId": 219578
            },
            {
                "examAnswerIds": [
                    959272
                ],
                "examQuestionId": 219579
            },
            {
                "examAnswerIds": [
                    959278
                ],
                "examQuestionId": 219580
            },
            {
                "examAnswerIds": [
                    959284
                ],
                "examQuestionId": 219581
            },
            {
                "examAnswerIds": [
                    959290
                ],
                "examQuestionId": 219582
            },
            {
                "examAnswerIds": [
                    959302
                ],
                "examQuestionId": 219584
            },
            {
                "examAnswerIds": [
                    959308
                ],
                "examQuestionId": 219585
            },
            {
                "examAnswerIds": [
                    959314
                ],
                "examQuestionId": 219586
            },
            {
                "examAnswerIds": [
                    959320
                ],
                "examQuestionId": 219587
            },
            {
                "examAnswerIds": [
                    959326
                ],
                "examQuestionId": 219588
            },
            {
                "examAnswerIds": [
                    959332
                ],
                "examQuestionId": 219589
            },
            {
                "examAnswerIds": [
                    959338
                ],
                "examQuestionId": 219590
            },
            {
                "examAnswerIds": [
                    959344
                ],
                "examQuestionId": 219591
            },
            {
                "examAnswerIds": [
                    959350
                ],
                "examQuestionId": 219592
            },
            {
                "examAnswerIds": [
                    959356
                ],
                "examQuestionId": 219593
            },
            {
                "examAnswerIds": [
                    959362
                ],
                "examQuestionId": 219594
            },
            {
                "examAnswerIds": [
                    959368
                ],
                "examQuestionId": 219595
            },
            {
                "examAnswerIds": [
                    959374
                ],
                "examQuestionId": 219596
            },
            {
                "examAnswerIds": [
                    959382
                ],
                "examQuestionId": 219597
            },
            {
                "examAnswerIds": [
                    959390
                ],
                "examQuestionId": 219598
            },
            {
                "examAnswerIds": [
                    959398
                ],
                "examQuestionId": 219599
            },
            {
                "examAnswerIds": [
                    959406
                ],
                "examQuestionId": 219600
            },
            {
                "examAnswerIds": [
                    959414
                ],
                "examQuestionId": 219601
            },
            {
                "examAnswerIds": [
                    959422
                ],
                "examQuestionId": 219602
            },
            {
                "examAnswerIds": [
                    959430
                ],
                "examQuestionId": 219603
            },
            {
                "examAnswerIds": [
                    959438
                ],
                "examQuestionId": 219604
            },
            {
                "examAnswerIds": [
                    959446
                ],
                "examQuestionId": 219605
            },
            {
                "examAnswerIds": [
                    959454
                ],
                "examQuestionId": 219606
            },
            {
                "examAnswerIds": [
                    959462
                ],
                "examQuestionId": 219607
            },
            {
                "examAnswerIds": [
                    959470
                ],
                "examQuestionId": 219608
            },
            {
                "examAnswerIds": [
                    959478
                ],
                "examQuestionId": 219609
            },
            {
                "examAnswerIds": [
                    959486
                ],
                "examQuestionId": 219610
            },
            {
                "examAnswerIds": [
                    959494
                ],
                "examQuestionId": 219611
            },
            {
                "examAnswerIds": [
                    959502
                ],
                "examQuestionId": 219612
            },
            {
                "examAnswerIds": [
                    959510
                ],
                "examQuestionId": 219613
            },
            {
                "examAnswerIds": [
                    959518
                ],
                "examQuestionId": 219614
            },
            {
                "examAnswerIds": [
                    959526
                ],
                "examQuestionId": 219615
            },
            {
                "examAnswerIds": [
                    959534
                ],
                "examQuestionId": 219616
            },
            {
                "examAnswerIds": [
                    959542
                ],
                "examQuestionId": 219617
            },
            {
                "examAnswerIds": [
                    959550
                ],
                "examQuestionId": 219618
            },
            {
                "examAnswerIds": [
                    959558
                ],
                "examQuestionId": 219619
            },
            {
                "examAnswerIds": [
                    959566
                ],
                "examQuestionId": 219620
            },
            {
                "examAnswerIds": [
                    959574
                ],
                "examQuestionId": 219621
            },
            {
                "examAnswerIds": [
                    959582
                ],
                "examQuestionId": 219622
            },
            {
                "examAnswerIds": [
                    959590
                ],
                "examQuestionId": 219623
            },
            {
                "examAnswerIds": [
                    959598
                ],
                "examQuestionId": 219624
            },
            {
                "examAnswerIds": [
                    959606
                ],
                "examQuestionId": 219625
            },
            {
                "examAnswerIds": [
                    959614
                ],
                "examQuestionId": 219626
            },
            {
                "examAnswerIds": [
                    959622
                ],
                "examQuestionId": 219627
            },
            {
                "examAnswerIds": [
                    959630
                ],
                "examQuestionId": 219628
            },
            {
                "examAnswerIds": [
                    959638
                ],
                "examQuestionId": 219629
            },
            {
                "examAnswerIds": [
                    959646
                ],
                "examQuestionId": 219630
            },
            {
                "examAnswerIds": [
                    959654
                ],
                "examQuestionId": 219631
            }
        ],
        "nickName": "junbotest",
        "countryCode": "CN",
        "email": "1255177725@qq.com",
        "sex": 1,
        "age": 1995,
        "deviceId": "16b641",
        "hl": "EN"
    }
    result = en_face.question_sub(payload=payload)
    orderNumber = GetKeyword.get_keyword(source=result, keyword='orderNumber')
    start_time = datetime.now()
    print(start_time)
    print(orderNumber)
    # for i in range(1000):
    # time.sleep(0.5)
    db = Database()
    sql = f"select ctime from t_exam_order_result where exam_order_id = (select exam_order_id from t_exam_order where order_number = '{orderNumber}') ;"
    result = db.readall(sql)
    print(result)
    if result != 'None':
        print(result)
    print(time.time())
