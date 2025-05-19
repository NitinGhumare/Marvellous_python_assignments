# 3. Write a program which accepts N numbers from the user and stores them into a list. Return the minimum number from that list.
# Example:

# Input: Number of elements: 4

# Input Elements: 13, 5, 45, 7

# Output: 5    


def Min_number(n):
    numbers = []
    for i in range(n):
        num = int(input("Enter element {i + 1}: "))
        numbers.append(num)
    return min(numbers)

if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    result = Min_number(n)
    print("Minimum number is :", result)
