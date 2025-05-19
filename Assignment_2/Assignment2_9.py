# Write a program which accepts a number from the user and returns the number of digits in that number.

# Input:
# 5187934
# Output:
# 7

def Digits(no):

    n = len(str(no))  

    print("the number of digits in number is : ",n)

if __name__=="__main__":

    n=input("enter the numbers: ")

    Digits(n)        



