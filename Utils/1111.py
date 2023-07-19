import json

# 提取响应结果,为字符串
result = prev.getResponseDataAsString()

# 提取结果转换为json类型
result_dic = json.loads(result)

# 获取所需要的数据列
# list=result_dic.get("data").get("children")

# 数据库查询该数据的数量,作为长度使用
count = int(vars.get("count_1"))

#     数据库查询出的数据,作为列表保存
list1 = [vars.get("cluster_id_" + str(i)) for i in range(1, count + 1)]

# json返回的数据,作为列表保存

# list2=[i.get("value") for i in result_dic.get("data")[0].get("children")]

# list3=[i.get("value") for i in result_dic.get("data")[1].get("children")]

# list2=list2+list3
list2 = []
for j in result_dic.get("data"):
    list = [i.get("itemName") for i in j.get("children") if j.get("dbVersion") == 5.7 and j.get("dbType")=="mysql"]
    list2 = list2 + list
for j in result_dic.get("data"):
    list = [i.get("itemName") for i in j.get("children") if j.get("dbVersion") == 5.7 and j.get("dbType")=="mysql"]
    list2 = list2 + list
for j in result_dic.get("data"):
    list = [i.get("itemName") for i in j.get("children") if j.get("dbVersion") == 5.7 and j.get("dbType")=="mysql"]
    list2 = list2 + list
# 两个列表都存在的元素
a = [x for x in list1 if x in list2]

# 两个列表中的不同元素
b = [y for y in (list1 + list2) if y not in a]

# #如果b列表为空,则说明所有元素相同,则断言成功

if b != []:
    msg = "equl faild " + str(len(list1)) + "___" + str(len(list2)) + "___different list" + str(b)
    AssertionResult.setFailureMessage(msg)
    AssertionResult.setFailure(True)
