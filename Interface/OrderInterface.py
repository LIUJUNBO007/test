"""
订单模块相关接口
"""
from Utils.SendMethod import SendMethod
from Utils.OperationConfig import OperationConfig
import json
from Interface.AddressInterface import AddressInterface
from Utils.GetKeyword import GetKeyword


class OrderInterface(object):
    def __init__(self):
        self.address = AddressInterface()
        config = OperationConfig()
        self.url = config.get_option('test', 'url')
        self.headers = json.loads(config.get_option('test', 'headers'))

    def confirm_order(self):
        """确认订单"""
        method = 'post'  # 不带参数
        url = self.url + '/order/generateConfirmOrder'
        return SendMethod.send_method(method=method, url=url, headers=self.headers)

    def generate_order(self, paytype):
        """生成订单"""
        method = 'post'  # 参数 JSON格式
        url = self.url + '/order/generateOrder'
        payload = {
            "memberReceiveAddressId": self.address.get_address_id(),  # 收货地址id
            "payType": paytype  # 支付方式
        }
        return SendMethod.send_method(method=method, url=url, json=payload, headers=self.headers)
        pass

    def get_order_id(self, paytype):
        """获取订单id"""
        result = self.generate_order(paytype)  # 请求生成订单接口
        return GetKeyword.get_keyword(result, 'orderId')

    def pay_success(self, paytype):
        """
        支付回调
        :param paytype: 支付方式
        :return:
        说明: 当按照目前写法,运行支付回调方法时,不需要再次执行生成订单接口
        """
        method = 'post'  # x-www-form-urlencoded格式
        url = self.url + '/order/paySuccess'
        payload = {'orderId': self.get_order_id(paytype)}
        return SendMethod.send_method(method=method, url=url, data=payload, headers=self.headers)


if __name__ == '__main__':
    # order = OrderInterface()
    # print(order.confirm_order())  # 确认订单: 成功的前提: 1.当购物车中的商品是系统中存在的商品时;2.当购物车为空
    # print(order.generate_order(1))  # 生成订单
    # print(order.pay_success(1))  # 支付回调
    a='''BSM
    CHG
    .V/1LZUH
    .F/CA1324/23DEC/PEK/J
    .N/3999948517001
    .S/Y/3C/C/049//Y
    .P/1HAOSHUAI
    .Y/CA001447467252.L/MLT6JV.T/159448
    ENDBSM'''
    # print(a)
    # b=a.replace('\n', '\\n')
    # print(b)
    print(repr('''BSM
    CHG
    .V/1LZUH
    .F/CA1324/23DEC/PEK/J
    .N/3999948517001
    .S/Y/3C/C/049//Y
    .P/1HAOSHUAI
    .Y/CA001447467252.L/MLT6JV.T/159448
    ENDBSM'''))









