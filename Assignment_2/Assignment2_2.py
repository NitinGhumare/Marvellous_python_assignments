# 2.2 Write a program which accept one number and display below pattern.
# Input : 5 

def Display(no):

    for i in range(no):
        print(" * " * 5 )

if __name__=="__main__":
    number=int(input("Enter the number: "))

Display(number)  
