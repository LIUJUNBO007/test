"""
文件名: GetKeyword.py
作用: 专门读取json格式的数据,从json数据中提取关键字所对应的值
使用库: jsonpath
安装jsonpath  pip install jsonpath

jsonpath.jsonpath(数据源,jsonpath表达式)
    - 数据源: json格式的数据
    - jsonpath表达式: $..status关键字  查找json文件中所有status的值,得到一个列表
"""
from jsonpath import jsonpath


class GetKeyword(object):
    @staticmethod
    def get_keyword(source, keyword):
        """
        通过关键字获取对应的值,如果有多个值,默认获取第一个,如果关键字不存在,返回FALSE
        :param source: 数据源,数据类型dict,list
        :param keyword: 关键字
        :return: 关键字对应的值
        """
        try:
            return jsonpath(source, f'$..{keyword}')[0]
        except:
            print(f'关键字{keyword}不存在')
            return False

    @staticmethod
    def get_keywords(source, keyword):
        """
        通过关键字获取对应的所有值,如果不存在,返回False
        :param source: 数据源
        :param keyword: 关键字
        :return:
        """
        try:
            return jsonpath(source, f'$..{keyword}')
        except:
            print(f'关键字{keyword}不存在')
            return False


if __name__ == '__main__':
    test_data = {
        'status_code': 200,
        'body': {
            'status': 10200,
            'message': 'add event success'
        },
        'headers': {
            'Date': 'Sun, 05 Sep 2021 09:08:08 GMT',
            'Server': 'WSGIServer/0.2 CPython/3.7.0',
            'Content-Type': 'application/json',
            'X-Frame-Options': 'DENY',
            'Content-Length': '49',
            'X-Content-Type-Options': 'nosniff',
            'Referrer-Policy': 'same-origin'
        },
        'response_time': 135,
        'status': '123456'
    }
    # data = '456'
    print(GetKeyword.get_keywords(source=test_data, keyword='Date'))
    print(2 ** 32 - 1)
    print(GetKeyword.get_keywords(source=test_data, keyword='Date'))
    for i in range(10):
        print(i)
    print(GetKeyword.get_keywords(source=test_data, keyword='Date'))
    print(GetKeyword.get_keywords(source=test_data, keyword='Date'))
