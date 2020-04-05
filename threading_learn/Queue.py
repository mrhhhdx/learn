import threading
import time
from queue import Queue

def job(l, q):
    for i in range(len(l)): #循环l列表中的值
        l[i] = l[i]**2 #每个列表中的元素进行平方的运算
    q.put(l) #多线程不能返回出一个值

def multithreading():
    q = Queue() #要在q中放入job计算出的返回值
    threads = [] #所有线程放在这个列表中
    data = [[1,2,3],[3,4,5],[5,5,5], [6,6,6]]
    for i in range(4): #定义四个线程
        t = threading.Thread(target=job, args=(data[i], q)) #开始设定线程，job后面没有括号，只是一个索引，参数加在args中
        t.start()
        threads.append(t) #将这个线程加到全部线程中
    for thread in threads: #附加到各自主线程上
        thread.join()
    results = [] #所有执行完后返回值
    for _ in range(4): #得到q中的值
        results.append(q.get()) #每次只能拿一个，按顺序拿出一个，所以要拿四次
    print(results)


if __name__ == '__main__' :
    multithreading()