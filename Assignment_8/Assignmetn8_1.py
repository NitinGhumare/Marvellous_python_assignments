# 1.
# Design a Python application which creates two threads named as even and odd.

# The even thread will display the first 10 even numbers.

# The odd thread will display the first 10 odd numbers.

import os 
import multiprocessing
import threading

def even(number):
    for i in range(2,number):
        if i % 2 == 0:
            print(i)

def odd(number):
    for i in range(1,number):
        if i % 2 != 0:
            print (i)

if __name__=="__main__":
    number=int(input("Enter the number : "))
    thread1=threading.Thread(target=even,args=(number,))
    thread2=threading.Thread(target=odd,args=(number,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


