"""
1. 学习目标
    掌握python操作ini文件的方法  读  写
2. 概念或作用
    配置文件: 存放项目中使用的一些常量
        环境地址
        数据库地址
        数据库端口号
        数据库用户名密码
3. 语法
    使用 configparser 库操作项目中的配置文件

4. 案例
"""
import configparser
import os


class OperationConfig(object):
    def __init__(self, filename='config.ini'):
        base_path = os.path.dirname(os.path.dirname(__file__))  # 项目目录
        config_path = os.path.join(base_path, 'Config')  # 配置文件目录
        self.file_path = os.path.join(config_path, filename)
        self.config = configparser.ConfigParser()
        self.config.read(self.file_path)

    def get_option(self, section, option):
        """
        获取指定节点的选项,如果存在,返回选项对应的值,反之,返回None
        :param section: 节点名称
        :param option: 选项名称
        :return:
        """
        # 判断节点和选项是否存在
        if self.config.has_section(section=section):  # 判断节点是否存在
            if self.config.has_option(section=section, option=option):  # 选项是否存在
                return self.config.get(section=section, option=option)  # 获取指定节点的选项
            else:
                print(f'选项{option}不存在')
                return None
        else:
            print(f'节点{section}不存在')
            return None

    def set_option(self, section, option, value=None):
        """给指定节点添加选项"""
        if self.config.has_section(section) is False:  # 判断节点是否存在
            self.config.add_section(section=section)  # 新增节点
        with open(self.file_path, 'r+') as fp:
            self.config.set(section=section, option=option, value=value)  # 写对应节点选项的值
            self.config.write(fp)


if __name__ == '__main__':
    config = OperationConfig()
    # print(config.get_option('test', 'url1'))
    config.set_option('dev','host','123456')
