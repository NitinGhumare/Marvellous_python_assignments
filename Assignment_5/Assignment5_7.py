# Q7. Area and Perimeter of Rectangle
# Task:
# Accept the length and width of a rectangle. Calculate and display the area and perimeter.

# Expected Input:
# Enter length: 5
# Enter width: 3

# Expected Output:
# Area: 15
# Perimeter: 16 

def Rectangle(l,w):
    Area = l * w

    print("The area of rectangle is : ",Area)

    Perimeter = ( l + w) * 2 

    print("The Perimeter of rectangle is : ",Perimeter)


if __name__ =="__main__":

    length=int(input("Enter length of rectangle: "))

    width = int(input("Enter width of rectangle : "))

    Rectangle(length,width)    