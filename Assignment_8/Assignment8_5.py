# 5. Design a Python application which contains two threads named as thread1 and thread2.

# Thread1 displays 1 to 50 on screen.

# Thread2 displays 50 to 1 in reverse order on screen.
# After execution of thread1 gets completed, then schedule thread2.

import threading 

def Display1():
    for i in range(1,51):
        print(i)

def Display2():
    for i in range(50,0,-1):
        print(i)

if __name__=="__main__":

    thread1=threading.Thread(target=Display1,args=())      

    thread2=threading.Thread(target=Display2,args=())   

    thread1.start()
    thread1.join() 
    

    thread2.start()
    thread2.join() 