# Use the DataFrame from Q1 and print descriptive statistics using .describe().

import pandas as pd 

def main():
    data= {'Name': ['Amit', 'Sagar', 'Pooja'],
            'Math': [85, 90, 78],
            'Science': [92, 88, 80],
            'English': [75, 85, 82]}
    df=pd.DataFrame(data)
    print(df)

    print("Stastical info of data are : ",df.describe())



if __name__=="__main__":
    main()