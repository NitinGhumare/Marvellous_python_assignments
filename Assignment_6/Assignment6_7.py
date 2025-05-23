# Q7. Find Maximum Number
# Problem: Accept 5 numbers from the user. Find and print the largest number.
# Expected Input:
# Enter 5 numbers: 23 89 12 56 45
# Expected Output:
# Maximum number is: 89


def DisplayMax(n):
    
    res=max(n)

    print("Maximum number is: ",res)

if __name__=="__main__":

    n = list(map(int, input("Enter 5 numbers: ").split()))

    DisplayMax(n)      