# 2.8. Pattern Display Program
# Question:
# Write a program which accepts one number and displays the below pattern.

# Input:
# 5
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

def Display(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()  # Move to next line after each row

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    Display(num)

