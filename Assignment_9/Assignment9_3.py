# Create a python programme that use multiprocessing.pool to compute factorails in the list 

import multiprocessing 
import multiprocessing.pool
import time 
import os 

def FactDisplay(no):
    print("PID is :",os.getpid())
    fact=1
    
    for i in range(1,no+1):
        fact=fact*i 

    return fact 

def main():
    Data = [23, 46, 41, 46, 71, 45, 73]
    result=[]

    start_time=time.time()

    p=multiprocessing.Pool()

    result=p.map(FactDisplay,Data)

    p.close()
    p.join()

    print(result)

    end_time=time.time ()
    print("Execution time is : ",end_time - start_time)

if __name__ == "__main__":
    main()




    
 