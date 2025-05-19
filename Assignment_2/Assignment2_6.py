
# 2.6 Write a program which accept one number and display below pattern.
# Input : 5

# * * * * *  
# * * * *  
# * * *  
# * *  
# *

def Display(n):
    while n > 0 :
        print("  * " * n)
        n -= 1

if __name__=="__main__":
    number=int(input("Enter the number: "))

Display(number)  