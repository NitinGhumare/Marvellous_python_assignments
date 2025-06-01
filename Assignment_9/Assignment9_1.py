# 1. Create a Python program that starts 3 threads,
# each printing numbers from 1 to 5 with a delay of 1 second.
# Use threading.Thread. 

import threading 
import time 

def Display1():
    for i in range(1,6):
        print(i)
        time.sleep(1)

def Display2():
    for i in range(1,6):
        print(i)
        time.sleep(1)

def Display3():
    for i in range(1,6):
        print(i)
        time.sleep(1)


if __name__=="__main__":
    start_time=time.time()

    thread1=threading.Thread(target=Display1,args=())
    thread2=threading.Thread(target=Display2,args=())
    thread3=threading.Thread(target=Display3,args=())

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    end_time=time.time()

    print("Time required for execution is:", end_time - start_time, "seconds")
