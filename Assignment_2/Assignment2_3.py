# #2.3 Write a program which accept one number from user and return its factorial.
# Input: 5
# Output: 120

def Factorial(value1):
    result=1

    for i in range(1,value1+1):
        result = result* i 

    print("The Factorial of number is:",result)    

    
if __name__=="__main__":
    number1=int(input("enter the number for factorial: "))
    Factorial(number1)