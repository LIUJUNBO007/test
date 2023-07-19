"""
模块名称: 会员模块
    模块中的每一个接口至少写一个方法,当接口存在关联时,还需要写对应接口的关联方法
    - 接口录入
    - 接口关联
"""
from Utils.SendMethod import SendMethod
from Utils.GetKeyword import GetKeyword
from Utils.OperationConfig import OperationConfig
import json


class MemberInterface(object):
    def __init__(self):
        self.config = OperationConfig()
        self.url = self.config.get_option('test', 'url')

    def get_auth_code(self, telephone):
        """
        请求获取验证码接口
        :param telephone: 手机号码
        :return:
        """
        method = 'get'  # 请求方式
        url = self.url + '/sso/getAuthCode'  # 请求地址
        payload = {'telephone': telephone}  # 请求参数
        return SendMethod.send_method(method=method, url=url, params=payload)  # 发起请求

    def get_authCode(self, telephone):
        """
        获取验证码
        :return:
        """
        result = self.get_auth_code(telephone)
        return GetKeyword.get_keyword(result, 'data')

    def member_register(self, username, password, telephone):
        """会员注册"""
        method = 'post'
        url = self.url + '/sso/register'
        payload = {  # 请求参数类型 x-www-form-urlencoded格式
            'username': username,
            'password': password,
            'telephone': telephone,
            'authCode': self.get_authCode(telephone)  # 验证码
        }
        return SendMethod.send_method(method=method, url=url, data=payload)

    def member_login(self, username, password):
        """会员登录"""
        method = 'post'  # 请求参数类型 x-www-form-urlencoded格式
        url = self.url + '/sso/login'
        payload = {'username': username, 'password': password}
        return SendMethod.send_method(method=method, url=url, data=payload)

    def get_member_token(self):
        """
        获取会员token
        :return:
        """
        result = self.member_login(username='18328070164', password='18328070164')
        token = GetKeyword.get_keyword(result, 'token')
        headers = {'Authorization': f'Bearer {token}'}
        # return headers
        # 将headers写入到配置文件中
        self.config.set_option('test', 'headers', json.dumps(headers))


if __name__ == '__main__':
    member = MemberInterface()
    telephone = '13800138000'
    username = 'Jerry'
    password = '123456'
    # print(member.get_auth_code(telephone))  # 请求验证码接口
    # print(member.member_register(username, password, telephone))  # 请求注册接口
    # print(member.member_login(username, password))  # 请求登录接口
    print(member.get_member_token())
