"""
存放购物车模块的所有接口
"""
from Utils.GetKeyword import GetKeyword
from Utils.SendMethod import SendMethod
from Utils.OperationConfig import OperationConfig
import json


class CartInterface(object):
    def __init__(self):
        config = OperationConfig()
        self.url = config.get_option('test', 'url')
        self.headers = json.loads(config.get_option('test', 'headers'))

    def add_cart(self, payload):
        """添加购物车接口"""
        method = 'post'  # 请求参数类型是JSON
        url = self.url + '/cart/add'
        return SendMethod.send_method(method=method, url=url, json=payload, headers=self.headers)

    def get_cart_list(self):
        """查看购物车列表"""
        method = 'get'
        url = self.url + '/cart/list'
        return SendMethod.send_method(method=method, url=url, headers=self.headers)

    def get_cart_list_id(self):
        """获取购物车列表所有商品ID,以列表形式保存"""
        result = self.get_cart_list()  # 请求生成订单接口
        return GetKeyword.get_keywords(result, 'id')

    def clear_cart_list(self):
        """清空购物车"""
        method = 'post'
        url = self.url + '/cart/clear'
        return SendMethod.send_method(method=method, url=url, headers=self.headers)

    def delete_cart_list(self, num):
        """删除购物车中的某个商品"""
        method = 'post'
        url = self.url + '/cart/delete'
        payload = {
            'ids': self.get_cart_list_id()[num]
        }
        return SendMethod.send_method(method=method, url=url, headers=self.headers,data=payload)

    def update_cart_quantity(self, num, quantity):
        """修改购物车中的某个商品数量"""
        method = 'get'
        url = self.url + '/cart/update/quantity'
        payload = {
            'id': self.get_cart_list_id()[num],
            'quantity': quantity
        }
        return SendMethod.send_method(method=method,url=url,params=payload,headers=self.headers)

if __name__ == '__main__':
    cart = CartInterface()
    payload = {
        "createDate": "2021-09-11T01:09:15.541Z",
        "deleteStatus": 0,
        "id": 0,
        "modifyDate": "2021-09-11T01:09:15.541Z",
        "price": 2699,
        "productAttr": '[{"key":"颜色","value":"黑色"},{"key":"容量","value":"32G"}]',
        "productBrand": "小米",
        "productCategoryId": 19,
        "productId": 27,
        "productName": "小米8 全面屏游戏智能手机 6GB+64GB 黑色 全网通4G 双卡双待",
        "productPic": "http://macro-oss.oss-cn-shenzhen.aliyuncs.com/mall/images/20180615/xiaomi.jpg",
        "productSkuCode": "201808270027001",
        "productSkuId": 98,
        "productSn": "7437788",
        "productSubTitle": "骁龙845处理器，红外人脸解锁，AI变焦双摄，AI语音助手小米6X低至1299，点击抢购",
        "quantity": 1
    }
    print(cart.add_cart(payload))  # 添加购物车
    print(cart.get_cart_list())
