# 3. Design a Python application which creates two threads as evenlist and oddlist.
# Both the threads accept list of integers as parameter.

# Evenlist thread adds all even elements from input list and displays the addition.

# Oddlist thread adds all odd elements from input list and displays the addition.

import threading 

def EvenList(even_list):
    even_sum = 0
    for i in even_list:
        even_sum=even_sum+i 
    print("The sum of even list is: ",even_sum)    

def OddList(odd_list):
    odd_sum=0
    for i in odd_list:
        odd_sum=odd_sum+i 

    print("The sum of odd numbers is: ",odd_sum)

if __name__=="__main__":

    Even_List= list(map(int,input("Entet the even numbers: ").split()))
    Odd_List= list(map(int,input("Entet the odd numbers: ").split()))

    thread1=threading.Thread(target=EvenList,args=(Even_List,))  
    thread2=threading.Thread(target=OddList,args=(Odd_List,))    

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()           



