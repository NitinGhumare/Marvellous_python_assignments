# 2.5 Write a program which accept one number for user and check whether number is prime or not.
# Input: 5
# Output: It is Prime Number

def prime_number(n):
    if n <= 1:
        print("Number is not prime")
        return

    for i in range(2, n):
        if n % i == 0:
            print("Number is not prime")
            return
    print("Number is prime")

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    prime_number(n)
