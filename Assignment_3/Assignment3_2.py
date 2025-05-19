# # 2. Write a program which accepts N numbers from the user and stores them into a list. Return the maximum number from that list.
# # Example:

# # Input: Number of elements: 7

# # Input Elements: 13, 5, 45, 7, 4, 56, 34

# # Output: 56 


def Max_number(n):
    numbers = []
    for i in range(n):
        num = int(input("Enter element {i + 1}: "))
        numbers.append(num)
    return max(numbers)

if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    result = Max_number(n)
    print("Maximum number is :", result)