# write a progrmme which sum up numbers from 1 to 10 million by using normal,threading and multiprocessing.
import multiprocessing 
import threading 
import os 
import time 


def fun(no):
    total = 0
    for i in range(1, no + 1):
        total += i
    print("Sum is:", total)

def normal_sum(no):
    start_time = time.time()
    fun(no)
    end_time = time.time()
    print("Execution time normal:", end_time - start_time, "seconds")

def threading_sum(no):
    start_time = time.time()

    thread = threading.Thread(target=fun, args=(no,))
    thread.start()
    thread.join()

    end_time = time.time()
    print("Execution time threading:", end_time - start_time, "seconds")

def main():
    no = 10000000

    # Normal
    normal_sum(no)

    # Threading
    threading_sum(no)

    # Multiprocessing
    start_time = time.time()

    data = [no]
    p = multiprocessing.Pool()
    result = p.map(fun, data)

    p.close()
    p.join()

    end_time = time.time()
    print("Execution time multiprocessing:", end_time - start_time, "seconds")

    print("Exit from main")

if __name__ == "__main__":
    main()





