#  Q5. Even or Odd Number Check
# Task: Write a program to check whether the entered number is even or odd.
# Expected Input:
# Enter a number: 17
# Expected Output:
# 17 is an odd number.


def EvenOdd(number):
    if number % 2 == 0:
        print("The number is Even")

    else:
        print("The number is odd ")

if __name__=="__main__":
    number=int(input("Enter the number:"))

    EvenOdd(number)