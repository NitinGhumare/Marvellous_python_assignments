# Q4. Accept a number and print its factorial using a for loop.
# Expected Input:

# Enter a number: 5

# Factorial of 5 is: 120

def Factorial(n):
    fact=1
    for i in range(1,n+1):

        fact=fact * i 

    print("The factoral of number is: ",fact)

if __name__=="__main__":
    n=int(input("Enter the number : "))

    Factorial(n)        

