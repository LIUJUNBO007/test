"""
收货地址模块
"""
from Utils.GetKeyword import GetKeyword
from Utils.SendMethod import SendMethod
from Utils.OperationConfig import OperationConfig
import json


class AddressInterface(object):
    def __init__(self):
        config = OperationConfig()
        self.url = config.get_option('test', 'url')
        self.headers = json.loads(config.get_option('test', 'headers'))

    def add_address(self, payload):
        """添加收货地址"""
        method = 'post'  # 请求参数类型JSON
        url = self.url + '/member/address/add'
        return SendMethod.send_method(method=method, url=url, json=payload, headers=self.headers)

    def get_address_list(self):
        """查看所有收货地址列表"""
        method = 'get'  # 请求参数类型JSON
        url = self.url + '/member/address/list'
        return SendMethod.send_method(method=method, url=url, headers=self.headers)

    def get_address_id(self):
        """获取收货地址id"""
        result = self.get_address_list()
        return GetKeyword.get_keyword(result, 'id')

    def get_address_ids(self):
        """获取所有收货地址id,返回一个列表"""
        result = self.get_address_list()
        return GetKeyword.get_keywords(result, 'id')

    def updata_address(self, num):
        """根据ID修改收货地址"""
        method = 'post'
        id = self.get_address_ids()[num]
        url = self.url + f'/member/address/update/{id}'
        payload = {
            "city": "成都市",
            "defaultStatus": 0,
            "detailAddress": "天府大道388号",
            "name": "Jerry",
            "phoneNumber": "13900139000",
            "postCode": "000000",
            "province": "广东省",
            "region": "武侯区"
        }
        return SendMethod.send_method(method=method, url=url, headers=self.headers, json=payload)

    def get_address_single(self, num):
        """查看单个收货地址"""
        method = 'get'  # 请求参数类型JSON
        id = self.get_address_ids()[num]
        url = self.url + f'/member/address/{id}'
        return SendMethod.send_method(method=method, url=url, headers=self.headers)

    def delete_address(self,num):
        method='post'
        id = self.get_address_ids()[num]
        url = self.url+ f'/member/address/delete/{id}'
        return SendMethod.send_method(method=method,url=url,headers=self.headers)

if __name__ == '__main__':
    address = AddressInterface()
    payload = {
        "city": "成都市",
        "defaultStatus": 0,
        "detailAddress": "天府大道388号",
        "name": "Jerry",
        "phoneNumber": "13900139000",
        "postCode": "000000",
        "province": "四川省",
        "region": "武侯区"
    }
    # address.add_address(payload)
    # print(address.get_addres_list())
    print(address.get_address_id())
