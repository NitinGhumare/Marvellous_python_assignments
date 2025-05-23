# Q6. Celsius to Fahrenheit Converter
# Task:
# Accept temperature in Celsius and convert it to Fahrenheit using the formula:
# F = (C × 9/5) + 32

# Expected Input:
# Enter temperature in Celsius: 25

# Expected Output:
# Temperature in Fahrenheit: 77.0°F  


def CelsiusToFahrenheit(temp):

    F = (temp * 9/5) + 32 

    print("The temperature in Fahrenment is : ",F )

if __name__=="__main__":

    temp=int(input("Enter the temperature in Celsius : "))

    CelsiusToFahrenheit(temp)

