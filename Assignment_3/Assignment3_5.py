# 5.
# Write a program which accepts N numbers from user and stores them into a list. Return the addition of all prime numbers from that list.

# Note: The main python file accepts N numbers from user and passes each number to ChkPrime() function which is part of a user-defined module named MarvellousNum. The name of the function from the main file should be ListPrime().

import marvellous

from marvellous import ChkPrime

def ListPrime():
    numbers = []
    n = int(input("Enter number of elements: "))
    
    for i in range(n):
        num = int(input("Enter element {i + 1}: "))
        numbers.append(num)
    
    prime_sum = 0
    for num in numbers:
        if ChkPrime(num):
            prime_sum += num

    return prime_sum

if __name__ == "__main__":
    result = ListPrime()
    print("Addition of prime numbers:", result)