# def fib_loop(n):
#     a,b=0,1
#     for i in range(n+1):
#         a,b=b,a+b
#     return a
#
#
# for i in range(20):
#     print(fib_loop(i),end=' ')
#
#
# print(fib_loop(10))
#
#
# a = [21,33,2,4,535,25,252,32,32,24,5,32]
# for j in range(len(a)-1):
#     for i in range(len(a)-1-j):
#         if a[i] > a[i+1]:
#             a[i],a[i+1] = a[i+1],a[i]
# print(a)
#
#
# #计算杨辉三角 普通法
# triangle = [[1],[1,1]]
# for i in range(2,6):
#     swap = triangle[i-1]
#     cul = [1]
#     for j in range(i-1):
#         cul.append(swap[j]+swap[j+1])
#     cul.append(1)
#     triangle.append(cul)
# print(triangle)
#
#
# lt = []
# for i in range(100,1000):
#     a = i // 100
#     b = (i%100) // 10
#     c = i % 10
#     if a**3 + b**3 + c**3 == i:
#         lt.append(i)
# for i in range(len(lt)-1):
#     print(lt[i],end = ", ")
# print(lt[-1])

from threading import Thread
import time
def run(a = None, b = None) :
    print(a, b)
    time.sleep(1)

t = Thread(target = run, args = ("this is a", "thread"))
#此时线程是新建状态

print(t.getName())#获得线程对象名称
print(t.isAlive())#判断线程是否还活着。
t.start()#启动线程
t.join()#等待其他线程运行结束
