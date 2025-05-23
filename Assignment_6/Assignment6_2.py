# Q2. Print Sum of Even Numbers Between 1 and 100
# Use a loop to find and print the sum of all even numbers from 1 to 100.

# Sum of even numbers between 1 to 100 is: 2550

def SumNo():
    sum=0

    for i in range(2,101):
         if i % 2==0:
              
              sum=sum+i 

    print("The sum of all even numbers is : ",sum)

if __name__=="__main__":

        SumNo()        

        

        


