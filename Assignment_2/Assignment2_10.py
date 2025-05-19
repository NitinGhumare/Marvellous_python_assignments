def Digits_Add(no):
    sum = 0
    for i in str(no):
        sum =sum+int(i)
    print("The sum of the digits is:",sum)

if __name__ == "__main__":
    n = input("Enter the number: ")
    Digits_Add(n)

   