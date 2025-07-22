# Q1:
# Detect outliers in the 'Salary' column using the IQR method.

# data = {'Salary': [25000, 27000, 29000, 31000, 50000, 100000]}
import pandas as pd 
import numpy as np 
# import matplotlib.pyplot as plt

def main():
    data = {'Salary': [25000, 27000, 29000, 31000, 50000, 100000]} 
    df = pd.DataFrame(data)


    q1 = np.percentile(df['Salary'], 25)
    q3 = np.percentile(df['Salary'], 75)
    IQR = q3 - q1

    lower_bound = q1 - 1.5 * IQR       
    upper_bound = q3 + 1.5 * IQR 

    # Detect outliers
    outliers = df[(df['Salary'] < lower_bound) | (df['Salary'] > upper_bound)]
    print("Outliers:\n", outliers)

if __name__ == "__main__":
    main()
