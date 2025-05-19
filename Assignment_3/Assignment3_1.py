# 1.
# Write a program which accepts N numbers from user and stores them into a list. Return the addition of all elements from that list.
# Example:

# Input: Number of elements = 6

# Input Elements: 13 5 45 7 4 56

# Output: 130

def Addition(n):
    numbers = []
    for i in range(n):
        num = int(input("Enter element {i + 1}: "))
        numbers.append(num)
    return sum(numbers)

if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    result = Addition(n)
    print("Addition of numbers is :", result)