"""
购物车流程
"""
import allure
import pytest

from Utils.Database import Database
from Utils.GetKeyword import GetKeyword


def setup_module():
    """清理会员账号,购物车和订单表数据"""
    delete_cart = """DELETE FROM oms_cart_item WHERE member_id = 29;"""
    db = Database()
    db.write(delete_cart)


@allure.feature('购物车')
@allure.story('添加购物车')
def test_cart(cart):
    # 1.添加购物车
    payload1 = {
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
    payload2 = {
        # "createDate": "2021-09-11T02:15:05.061Z",
        # "deleteStatus": 0,
        # "id": 0,
        # "memberId": 0,
        # "memberNickname": "string",
        # "modifyDate": "2021-09-11T02:15:05.061Z",
        "price": 649,
        "productAttr": '[{"key":"颜色","value":"银色"},{"key":"容量","value":"16G"}]',
        "productBrand": "小米",
        "productCategoryId": 19,
        "productId": 28,
        "productName": "小米 红米5A 全网通版 3GB+32GB 香槟金 移动联通电信4G手机 双卡双待",
        "productPic": "shenzhen.aliyuncs.com/mall/images/20180615/5a9d248cN071f4959.jpg",
        "productSkuCode": "201808270028003",
        "productSkuId": 104,
        "productSn": "7437789",
        "productSubTitle": "8天超长待机，137g轻巧机身，高通骁龙处理器小米6X低至1299，点击抢购",
        "quantity": 1
    }
    cart.add_cart(payload1)  # 请求添加购物车接口
    cart.add_cart(payload2)  # 请求添加购物车接口
    # 断言数据库oms_cart_item表中新增了一条记录
    cart_sql = """SELECT id,delete_status FROM oms_cart_item WHERE member_id = 29;"""
    cart_sql_result = Database().readall(cart_sql)
    # print(cart_sql_result)
    # print(GetKeyword.get_keywords(cart_sql_result, 'delete_status'))
    pytest.assume(GetKeyword.get_keywords(cart_sql_result, 'delete_status') == [0, 0])  # 断言新增的购物车记录,delete_status值为0

    # 更改数量

@allure.feature('购物车')
@allure.story('查看购物车')
def test_cart_list(cart):
    get_cart_list_result=cart.get_cart_list()

    cart_sql = """SELECT id,delete_status FROM oms_cart_item WHERE member_id = 29;"""
    cart_sql_result = Database().readall(cart_sql)
    print(GetKeyword.get_keywords(get_cart_list_result, 'delete_status'))
    cart_list=GetKeyword.get_keywords(get_cart_list_result, 'deleteStatus')
    pytest.assume(GetKeyword.get_keywords(cart_sql_result, 'delete_status') ==cart_list)



@allure.feature('购物车')
@allure.story('购物车修改数量')
def test_cart_update(cart):
    cart.update_cart_quantity(num=1, quantity=5)
    quantity_sql = """SELECT id,quantity FROM oms_cart_item WHERE member_id = 29;"""
    quantity_sql_result = Database().readall(quantity_sql)
    # print(quantity_sql_result)
    # print(GetKeyword.get_keywords(quantity_sql_result, 'quantity'))
    pytest.assume(GetKeyword.get_keywords(quantity_sql_result, 'quantity')[1] == 5)  # 断言数量的更改


# 删除第二个商品
@allure.feature('购物车')
@allure.story('删除购物车指定商品')
def test_delete_cart(cart):
    cart.delete_cart_list(1)  # 删除第二个商品
    delete_sql = """SELECT id,quantity,delete_status FROM oms_cart_item WHERE member_id = 29;"""
    delete_sql_result = Database().readall(delete_sql)
    pytest.assume(GetKeyword.get_keywords(delete_sql_result, 'delete_status') == [0, 1])  # 断言删除商品状态

    # 清空


@allure.feature('购物车')
@allure.story('清空购物车')
def test_clear_cart(cart):
    cart.clear_cart_list()
    clear_sql = """SELECT id,quantity,delete_status FROM oms_cart_item WHERE member_id = 29;"""
    clear_sql_result = Database().readall(clear_sql)
    pytest.assume(GetKeyword.get_keywords(clear_sql_result, 'delete_status') == [1, 1])  # 断言清空后所有商品状态


if __name__ == '__main__':
    pytest.main()
