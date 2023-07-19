"""
地址操作流程
"""
import allure
import pytest
from Utils.Database import Database
from Utils.GetKeyword import GetKeyword


def setup_module():
    """清理会员账号,购物车和订单表数据"""
    delete_address = """DELETE FROM ums_member_receive_address WHERE member_id = 29;"""
    db = Database()
    db.write(delete_address)



# class test_address_flow():
@allure.feature('地址')
@allure.story('添加地址')
def test_address(address):
    """添加地址"""
    payload1 = {
        "city": "成都市",
        "defaultStatus": 0,
        "detailAddress": "天府大道388号",
        "name": "Jerry",
        "phoneNumber": "13900139000",
        "postCode": "000000",
        "province": "山东省",
        "region": "武侯区"
    }
    payload2 = {
        "city": "成都市",
        "defaultStatus": 0,
        "detailAddress": "天府大道388号",
        "name": "Jerry",
        "phoneNumber": "13900139000",
        "postCode": "000000",
        "province": "四川省",
        "region": "武侯区"
    }
    payload3 = {
        "city": "成都市",
        "defaultStatus": 0,
        "detailAddress": "天府大道388号",
        "name": "Jerry",
        "phoneNumber": "13900139000",
        "postCode": "000000",
        "province": "台湾省",
        "region": "武侯区"
    }
    address.add_address(payload=payload1)
    address.add_address(payload=payload2)
    address.add_address(payload=payload3)
    address_sql = """SELECT * from ums_member_receive_address WHERE member_id = 29;"""
    address_sql_result = Database().readall(address_sql)
    # print(GetKeyword.get_keywords(address_sql_result, 'province'))
    # print(11111111111111111111111111111111111111111111111111111111111111111111111111111)
    pytest.assume(GetKeyword.get_keywords(address_sql_result, 'province') == ['山东省', '四川省', '台湾省'])  # 断言添加省份是否与数据库相同

@allure.feature('地址')
@allure.story('查询地址')
def test_address_list(address):
    # 1 查询地址列表
    address_list_result = address.get_address_list()
    province_result = GetKeyword.get_keywords(address_list_result, 'province')  # 查询响应中的省份信息
    # print(province_result)
    address_sql = """SELECT * from ums_member_receive_address WHERE member_id = 29;"""  # 数据库语句
    address_sql_result = Database().readall(address_sql)  # 查询数据库数据,返回值为列表
    # 断言查看的省份是否与数据库查询省份相同
    pytest.assume(GetKeyword.get_keywords(address_sql_result, 'province') == province_result)

@allure.feature('地址')
@allure.story('查询单个地址')
def test_address_single(address):
    # 2 查询单个地址
    address_single_result = address.get_address_single(num=1)  # 查询第二个地址
    # print(address_single_result)
    province_single_result = GetKeyword.get_keyword(address_single_result, 'province')  # 查询地址中的省份
    # print(province_single_result)
    address_sql = """SELECT * from ums_member_receive_address WHERE member_id = 29;"""  # 数据库语句
    address_sql_result = Database().readall(address_sql)  # 查询数据库数据,返回值为列表
    # 断言查看的省份是否与数据库查询省份相同
    pytest.assume(province_single_result == GetKeyword.get_keywords(address_sql_result, 'province')[1])

@allure.feature('地址')
@allure.story('修改地址')
def test_address_updata(address):
    # 3 修改收货地址
    address.updata_address(1)
    address_updata_result = address.get_address_single(num=1)  # 查询第二个地址
    # print(address_single_result)
    province_updata_result = GetKeyword.get_keyword(address_updata_result, 'province')
    address_sql = """SELECT * from ums_member_receive_address WHERE member_id = 29;"""  # 数据库语句
    address_sql_result = Database().readall(address_sql)  # 查询数据库数据,返回值为列表
    # 断言查看的省份是否与数据库查询省份相同
    pytest.assume(province_updata_result == GetKeyword.get_keywords(address_sql_result, 'province')[1])

@allure.feature('地址')
@allure.story('删除地址')
def test_address_delete(address):
    # # 4.删除收货地址
    address.delete_address(1)
    address_delete_result = address.get_address_single(num=1)  # 查询删除的地址
    print(address_delete_result)
    province_delete_result = GetKeyword.get_keyword(address_delete_result, 'province')
    address_sql = """SELECT * from ums_member_receive_address WHERE member_id = 29;"""  # 数据库语句
    address_sql_result = Database().readall(address_sql)  # 查询数据库数据,返回值为列表
    pytest.assume(
        province_delete_result == GetKeyword.get_keywords(address_sql_result, 'province')[1])  # 断言删除后是否下一位默认地址变为第二个


if __name__ == '__main__':
    pytest.main()