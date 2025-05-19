2.1# Create one module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for multiplication and Div() for division. 
# All functions accepts two parameters as number and perform the operation. 
# Write on python program which call all the functions from Arithmetic module by accepting the parameters from user.
import Arithmetic

def main():
    value1=int(input("enter the 1st number: "))
    value2=int(input("enter the 2nd number: "))

    print("Addition of two number is : ",Arithmetic.add(value1,value2))
    print("subtraction of two number is : ",Arithmetic.sub(value1,value2))
    print("multiplication of two number is : ",Arithmetic.mul(value1,value2))
    print("Division of two number is : ",Arithmetic.div(value1,value2))


if __name__=="__main__":
    main()