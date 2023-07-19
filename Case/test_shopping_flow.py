"""
购物流程测试用例
    - 1.购买不参与营销活动的商品
    - 2.购买满减商品
    - 3.购买折扣商品
    - 4.购买满减+折扣
"""
import allure
import pytest
from Utils.Database import Database
from Utils.GetKeyword import GetKeyword


def setup():
    """清理会员账号,购物车和订单表数据"""
    delete_cart = """DELETE FROM oms_cart_item WHERE member_id = 29;"""
    delete_order = """DELETE FROM oms_order WHERE member_id = 29;"""
    db = Database()
    db.write(delete_order)
    db.write(delete_cart)


@allure.feature('购物流程')
@allure.story('购物不参与活动商品')
def test_general_shopping(cart, order):
    """购买不参与营销活动的商品"""
    # 0.检查购买前商品的库存
    stock_sql = """SELECT stock FROM pms_sku_stock WHERE id = 98;"""
    stock_sql_result = Database().readone(stock_sql)
    stock_before = GetKeyword.get_keyword(stock_sql_result, 'stock')  # 购买前的库存
    # 1.添加购物车
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
    cart.add_cart(payload)  # 请求添加购物车接口
    # 断言数据库oms_cart_item表中新增了一条记录
    cart_sql = """SELECT id,delete_status FROM oms_cart_item WHERE member_id = 29"""
    cart_sql_result = Database().readone(cart_sql)
    pytest.assume(GetKeyword.get_keyword(cart_sql_result, 'delete_status') == 0)  # 断言新增的购物车记录,delete_status值为0
    # 2.确认订单
    confirm_result = order.confirm_order()
    pay_amount = GetKeyword.get_keyword(confirm_result, 'payAmount')  # 获取应付金额
    pytest.assume(pay_amount == payload['price'])  # 断言应付金额和商品价格相同
    # 3.生成订单
    # 4.支付回调
    order.pay_success(1)
    # 断言订单表中是否新增了一条记录,status=1
    order_sql = """SELECT id,`status` FROM oms_order WHERE member_id = 29 ORDER BY id DESC LIMIT 1;"""
    order_sql_result = Database().readone(order_sql)
    pytest.assume(GetKeyword.get_keyword(order_sql_result, 'status') == 1)  # 断言订单支付状态
    pay_cart_result = Database().readone(cart_sql)
    pytest.assume(GetKeyword.get_keyword(pay_cart_result, 'delete_status') == 1)  # 断言订单生成后,delete_status=1
    stock_sql_result = Database().readone(stock_sql)
    stock_after = GetKeyword.get_keyword(stock_sql_result, 'stock')  # 购买后的库存
    pytest.assume(stock_before - stock_after == payload['quantity'])  # 断言库存是否减少


@allure.feature('购物流程')
@allure.story('购物满减活动活动商品')
def test_full_reduce_shopping(cart, order):
    """购买参与满减活动的商品"""
    # 0.检查购买前商品的库存
    stock_sql = """SELECT stock FROM pms_sku_stock WHERE id = 104;"""
    stock_sql_result = Database().readone(stock_sql)
    stock_before = GetKeyword.get_keyword(stock_sql_result, 'stock')  # 购买前的库存
    # 1.添加购物车
    payload = {
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

    cart.add_cart(payload)  # 请求添加购物车接口
    # 断言数据库oms_cart_item表中新增了一条记录
    cart_sql = """SELECT id,delete_status FROM oms_cart_item WHERE member_id = 29"""
    cart_sql_result = Database().readone(cart_sql)
    pytest.assume(GetKeyword.get_keyword(cart_sql_result, 'delete_status') == 0)  # 断言新增的购物车记录,delete_status值为0
    # 2.确认订单
    confirm_result = order.confirm_order()
    pay_amount = GetKeyword.get_keyword(confirm_result, 'payAmount')  # 获取应付金额
    pytest.assume(pay_amount == payload['price'] - 50)  # 断言应付金额和商品价格相同
    # 3.生成订单
    # 4.支付回调
    order.pay_success(1)
    # 断言订单表中是否新增了一条记录,status=1
    order_sql = """SELECT id,`status` FROM oms_order WHERE member_id = 29 ORDER BY id DESC LIMIT 1;"""
    order_sql_result = Database().readone(order_sql)
    pytest.assume(GetKeyword.get_keyword(order_sql_result, 'status') == 1)  # 断言订单支付状态
    pay_cart_result = Database().readone(cart_sql)
    pytest.assume(GetKeyword.get_keyword(pay_cart_result, 'delete_status') == 1)  # 断言订单生成后,delete_status=1
    stock_sql_result = Database().readone(stock_sql)
    stock_after = GetKeyword.get_keyword(stock_sql_result, 'stock')  # 购买后的库存
    pytest.assume(stock_before - stock_after == payload['quantity'])  # 断言库存是否减少


@allure.feature('购物流程')
@allure.story('购物折扣活动商品')
def test_discount_shopping(cart, order):
    """购买参与折扣活动的商品"""
    # 0.检查购买前商品的库存
    stock_sql = """SELECT stock FROM pms_sku_stock WHERE id =101;"""
    stock_sql_result = Database().readone(stock_sql)
    stock_before = GetKeyword.get_keyword(stock_sql_result, 'stock')  # 购买前的库存
    # 1.添加购物车
    payload = {
        # "createDate": "2021-09-11T02:15:05.061Z",
        # "deleteStatus": 0,
        # "id": 0,
        # "memberId": 0,
        # "memberNickname": "string",
        # "modifyDate": "2021-09-11T02:15:05.061Z",
        "price": 2999,
        "productAttr": '[{"key":"颜色","value":"蓝色"},{"key":"容量","value":"64G"}]',
        "productBrand": "小米",
        "productCategoryId": 19,
        "productId": 27,
        "productName": "小米8 全面屏游戏智能手机 6GB+64GB 黑色 全网通4G 双卡双待",
        "productPic": "http://macro-oss.oss-cn-shenzhen.aliyuncs.com/mall/images/20180615/xiaomi.jpg",
        "productSkuCode": "201808270027004",
        "productSkuId": 101,
        "productSn": "7437788",
        "productSubTitle": "骁龙845处理器，红外人脸解锁，AI变焦双摄，AI语音助手小米6X低至1299，点击抢购",
        "quantity": 2
    }

    cart.add_cart(payload)  # 请求添加购物车接口
    # 断言数据库oms_cart_item表中新增了一条记录
    cart_sql = """SELECT id,delete_status FROM oms_cart_item WHERE member_id = 29"""
    cart_sql_result = Database().readone(cart_sql)
    pytest.assume(GetKeyword.get_keyword(cart_sql_result, 'delete_status') == 0)  # 断言新增的购物车记录,delete_status值为0
    # 2.确认订单
    confirm_result = order.confirm_order()
    pay_amount = GetKeyword.get_keyword(confirm_result, 'payAmount')  # 获取应付金额
    pytest.assume(int(pay_amount) == int(payload['price'] * 1.6))  # 断言应付金额和商品价格相同
    # 3.生成订单
    # 4.支付回调
    order.pay_success(1)
    # 断言订单表中是否新增了一条记录,status=1
    order_sql = """SELECT id,`status` FROM oms_order WHERE member_id = 29 ORDER BY id DESC LIMIT 1;"""
    order_sql_result = Database().readone(order_sql)
    pytest.assume(GetKeyword.get_keyword(order_sql_result, 'status') == 1)  # 断言订单支付状态
    pay_cart_result = Database().readone(cart_sql)
    pytest.assume(GetKeyword.get_keyword(pay_cart_result, 'delete_status') == 1)  # 断言订单生成后,delete_status=1
    stock_sql_result = Database().readone(stock_sql)
    stock_after = GetKeyword.get_keyword(stock_sql_result, 'stock')  # 购买后的库存
    pytest.assume(stock_before - stock_after == payload['quantity'])  # 断言库存是否减少


if __name__ == '__main__':
    pytest.main()
