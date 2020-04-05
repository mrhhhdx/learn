import  threading
import time

def thread_job():
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.1)
    print('T1 finish\n')
def T2_job():
    print('T2 start\n')
    print('t2 FINISH\n')

def main():
    added_thread = threading.Thread(target=thread_job, name='T1')
    thread2 = threading.Thread(target=T2_job, name='T2')
    '''print(threading.active_count())
    print(threading.enumerate())
    print(threading.current_thread())'''
    added_thread.start()
    thread2.start()
    thread2.join()
    added_thread.join() #这句后面的语句在T1 thread结束后执行
    print('all done\n')

if __name__ == '__main__' :
    main()