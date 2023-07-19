# #列表1
list1 = ['张三', '李四', '王五', '老二']
#列表2
list2 = ['张三', '李四', '老二', '王七']

a = [x for x in list1 if x in list2] #两个列表表都存在
b = [y for y in (list1 + list2) if y not in a] #两个列表中的不同元素

print('a的值为:',a)
print('b的值为:',b)

c = [x for x in list1 if x not in list2] #在list1列表中而不在list2列表中
d = [y for y in list2 if y not in list1] #在list2列表中而不在list1列表中
print('c的值为:',c)
print('d的值为:',d)
#
#
# data:{"clusterList": [
#     {
#         "key": "C21122100015",
#         "val": "test02",
#         "isSelected": false
#     },
#     {
#         "key": "C21122100027",
#         "val": "test03",
#         "isSelected": false
#     },
#     {
#         "key": "C21122100026",
#         "val": "ORCLDG",
#         "isSelected": false
#     },
#     {
#         "key": "C21122100025",
#         "val": "test02",
#         "isSelected": false
#     }
# ]}
#
# list=vars.get("data").get("clusterlis")
# for i in range(len(list)):
#     #     数据库查询出的数据
# list3=[vars.get("clustetlsi_"+str(i)) for i in range(len(list))]
# #    json返回的数据
# list4=[i.get("key") for i in vars.get("data").get("clusterlis")]
# #两个列表都存在
# a = [x for x in list1 if x in list2]
# #两个列表中的不同元素
# b = [x for x in (list1 + list2) if x not in a]
#如果b列表为空 则断言成功
from time import sleep
from tqdm import  trange
import pymysql

for i in trange(100):
    sleep(1)
