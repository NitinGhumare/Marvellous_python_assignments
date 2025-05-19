# 1.
# Write a program that contains one lambda function which
# accepts one parameter and returns that number’s power of two.

# Input : 4   →  Output : 16
# Input : 6   →  Output : 64


power = lambda A : A**2 

num=[4,6]

for i in num:
    result=power(i)

    print("The power of {i} is ",result)


