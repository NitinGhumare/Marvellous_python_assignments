# Q1. Arithmetic Operations on Two Numbers
# Task:
# Write a program to accept two integers from the user and display their:

# Sum

# Difference

# Product

# Division

# Enter first number: 10  
# Enter second number: 2  


# Sum: 12  
# Difference: 8  
# Product: 20  
# Division: 5.0  


def Sum(value1,value2):

    result_sum=value1+value2 

    print("Sum of two numbers is : ",result_sum)

    

def Diff(value1,value2):

    result_diff=value1-value2 

    print("Diff of two numbers is : ",result_diff)

    


def Prod(value1,value2):

    result_Prod=value1 * value2 

    print("Prod of two numbers is : ",result_Prod)

   


def Div(value1,value2):

    result_div=value1 / value2 

    print("Div of two numbers is : ",result_div)

  

if __name__=="__main__":

     


    value1=(int(input("Enter first number: ")))
    value2=(int(input("Enter Second number: ")))
    
    
    Sum(value1,value2)
    Diff(value1,value2)
    Prod(value1,value2)
    Div(value1,value2) 




