##2.4 Write a program which accept one number from user and return addition of its factors.
# Input: 12
# Output: 16 (1+2+3+4+6)    

def Factorial_add():
    res_add=0
    for i in range(1,n+1):
        res_add=res_add+i 

    return res_add

if __name__=="__main__":
    n=int(input("enter the number of addtion of factorals: "))

    result=Factorial_add()

    print("The addtion of factorals number is: ",result)
