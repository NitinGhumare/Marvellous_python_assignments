#  #2.7 Write a program which accept one number and display below pattern.
# Input: 5   
# 1 2 3 4 5  
# 1 2 3 4 5  
# 1 2 3 4 5  
# 1 2 3 4 5  
# 1 2 3 4 5  

def Display():
    for i in range(n):
        for j in range(1, n + 1):
            print(j, end=" ")
        print()

if __name__ == "__main__":
    n=int(input("Enter the number: "))
    Display()
