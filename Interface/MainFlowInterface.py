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


class MainFlowInterface(object):
    def __init__(self):
        config = OperationConfig()
        self.url = config.get_option('test', 'url')
        self.headers = json.loads(config.get_option('test', 'headers'))

    def order_info(self, payload):
        method = 'post'
        url = self.url + '/api/exam/order/info'
        return SendMethod.send_method(method=method, url=url, json=payload)

    def pay_order(self, payload):
        method = 'post'
        url = self.url + '/api/order/pay/generate/pay/order'
        return SendMethod.send_method(method=method, url=url, json=payload)

    def check_status(self, payload):
        method = 'post'
        url = self.url + '/api/order/pay/check/status'
        return SendMethod.send_method(method=method, url=url, json=payload)

    def get_auth_code(self, payload):
        method = 'get'  # 请求方式
        url = self.url + '/api/exam/order/info'  # 请求地址
        return SendMethod.send_method(method=method, url=url, params=payload)  # 发起请求


if __name__ == '__main__':
    fp = MainFlowInterface()
    current_time = datetime.now()
    # 偏移5分钟
    offset = timedelta(minutes=5)
    new_time = current_time - offset
    # 将新时间格式化为字符串
    new_time_str = new_time.strftime("%Y-%m-%dT%H:%M:%S")
    current_time_str = current_time.strftime("%Y-%m-%dT%H:%M:%S")
    # 1.提交答题表单
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
    result = (fp.order_info(payload=payload))
    orderNumber = GetKeyword.get_keyword(source=result, keyword='orderNumber')
    print(orderNumber)
    # 2.pay_oder
    payload = {
        "bizType": "20",
        "country": "CN",
        "orderNumber": f"{orderNumber}",
        "paymentType": "CREDITCART",
        "sukPackageId": "44",
        "redirectUrl": f"https://taotan.front.test.cdtaotan.com/pay_success/16b641/1511/IIQQ?hl=EN&orderNumber=${orderNumber}&bizType=20&prm44&email=1255177725@qq.com"
    }
    fp.pay_order(payload=payload)
    # 3.状态查询
    payload = {
        "bizType": "20",
        "orderNumber": f"{orderNumber}"
    }
    fp.check_status(payload=payload)
    # 4.订单信息
    payload = {'orderNumber': orderNumber}
    fp.get_auth_code(payload=payload)
