
# Q6. Triangle Pattern using Nested Loops
# Problem: Print Triangle Pattern using Nested Loops
# Expected Output:
# *
# * *
# * * *
# * * * *

def Display(n):

    for i in range(1,n+1):

        for j in range(i):
            print("*",end=" ")

        print()    

if __name__=="__main__":
    n=int(input("Enter the number: "))

    Display(n)        