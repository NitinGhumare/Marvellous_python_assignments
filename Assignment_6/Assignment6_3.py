# Q3. Accept a number from the user and print its multiplication table up to 10.

# Expected Input:

# Enter a number: 7

# Expected Output:

# 7 x 1 = 7  
# 7 x 2 = 14  
# ...  
# 7 x 10 = 70

def MultiPlication(n):
    mul=1
    for i in range(1,11):

        res=n*i

        print(n, "*" ,i,"=",res)

if __name__ == "__main__":

    n=int(input("Enter the number: "))

    MultiPlication(n)   
                  
       
