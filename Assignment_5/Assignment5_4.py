#  Q4. Find Largest Among Three Numbers
# Task: Accept three numbers from the user and print the largest using nested if-else statements.
# Expected Input:
# Enter three numbers: 5 9 3
# Expected Output:
# Largest number is 9.

def LargestNo(a,b,c):
    if a >= b:
        if a >= c:
            print("largetst number is : ",a )

        else:
            print("largest number is :",c)

    else:
        if b >= c:
            print("largest number is : ",b)

        else:
            print("largest number is : ",c)   

if __name__=="__main__":
    a=int(input("Enter the first no : "))
    b=int(input("Enter the second number: "))
    c=int(input("Enter the third number: "))

    LargestNo(a,b,c)                             