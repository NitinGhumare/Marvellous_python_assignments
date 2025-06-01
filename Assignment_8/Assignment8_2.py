# 2.
# Design a Python application which creates two threads as evenfactor and oddfactor.

# Both threads accept one parameter as an integer.

# Evenfactor thread will display the addition of even factors of the given number.

# Oddfactor thread will display the addition of odd factors of the given number.

# After execution of both, the main thread should display the message: “exit from main”.
import multiprocessing
import os 
import threading

def EvenFactor(number):
    sum=0
    for i in range(1,number):
        if number % i == 0 and i % 2 == 0:
            sum=sum+i 
    print("Addition of even factors:",sum)

def OddFactor(number):      
    sum=0
    for i in range(1,number):
        if number % i == 0 and i % 2 != 0:
            sum=sum+i 
    print("Addition of odd factors:",sum)

if __name__=="__main__":
    number=int(input("Enter the number : "))
    thread1=threading.Thread(target=EvenFactor,args=(number,))
    thread2=threading.Thread(target=OddFactor,args=(number,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()  

    print("exit from main")               


