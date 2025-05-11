#1. Write a program which contains one function named as Fun().That function should display "Hello from Fun" on console.

def Fun():
    print("Hello from Fun")

if __name__=="__main__":
    Fun()

#2. Write a program which contains one function named as ChkNum() which accepts one parameter as number.
# If the number is even, it should display "Even number", otherwise display "Odd number" on console.
# Input: 11 → Output: Odd Number
# Input: 8 → Output: Even Number

num=int(input("enter the number: "))

def ChkNum(num1):
    if num1 % 2 ==0:
        print("even number")
    else:
        print("odd number")

if __name__=="__main__":
    ChkNum(num)

#3 Write a program which contains one function named as Add() which accepts two numbers from the user and returns the addition of those two numbers.
# Input: 11, 5 → Output: 16

def Add(value1, value2):
    result = value1 + value2
    return result

if __name__ == "__main__":
    
    value1 = int(input("Enter 1st number: "))
    value2 = int(input("Enter 2nd number: "))
    result = Add(value1, value2)
    print("Addition of two numbers is:", result)



#4 Write a program which displays the word "Marvellous" five times on the screen.
def Display():
    for i in range(5):
        print("Marvellous") 
if __name__=="__main__":
    Display()



#5. Write a program which displays numbers from 10 to 1 on the screen.
# Output: 10 9 8 7 6 5 4 3 2 1

def Display():
    for no in range(10,0,-1):
        print(no)

if __name__=="__main__":
    Display()   


#6) Write a program which accepts a number from the user and checks whether that number is positive, negative, or zero.

# Input: 11 → Output: Positive Number

# Input: -8 → Output: Negative Number

# Input: 0 → Output: Zero



def main(no):
    if no > 0:
        print("no  is positive")

    elif no < 0:
        print("no is negative")   

    else:
        print("no is zero")    


if __name__=="__main__":

    no=int(input("enter the number: "))

    main(no)   



# 7.
# Write a program which contains one function that accepts one number from the user and returns true if the number is divisible by 5, otherwise return false.

# Input: 8 → Output: False

# Input: 25 → Output: True
def main(no):
    if no % 5 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    no = int(input("Enter the number: "))
    result = main(no)
    print("Output:", result)


# 8.
# Write a program which accepts a number from the user and prints that number of * on the screen.

# Input: 5 → Output: * * * * * 

def main(no):

    for i in range(no):
        print('*',end=" ")

if __name__ =="__main__":
    no= int(input("Please enter the number: "))

    main(no)   


# 9.
# Write a program which displays the first 10 even numbers on screen.

# Output: 2 4 6 8 10 12 14 16 18 20    

def Display_even():
    for i in range(2,21):
        if i % 2==0:
            print(i,end=" ")

if __name__=="__main__":
    Display_even()


# 10.
# Write a program which accepts a name from the user and displays the length of its name.

# Input: Marvellous → Output: 10    

def Display_name(name):

    output=len(name)

    print("the length of name is : ",output)

if __name__== "__main__":
    name=input("enter the name: ")
    Display_name(name)        

          










