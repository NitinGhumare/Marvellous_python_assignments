# 2. Write a Python program using multiprocessing.Process
# to square a list of numbers using multiple processes. 

import multiprocessing 
import time 


def SquareDisplay(numbers):
    for i in numbers:
        print(i**2)


def main():
    numbers=list(map(int,input("Enter the numbers: ").split()))

    start_time = time.time()

    T1=multiprocessing.Process(target=SquareDisplay,args=(numbers,))

    T1.start()
    T1.join()

    end_time = time.time()

    print("Time requred for execution is : ",end_time - start_time)

    print("end of main") 
   

if __name__=="__main__":
    main() 



    
                         

