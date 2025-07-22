# Q1: Normalize the 'Math' scores using Min-Max scaling.

import pandas as pd 

def main():
    data= {'Name': ['Amit', 'Sagar', 'Pooja'],
            'Math': [85, 90, 78],
            'Science': [92, 88, 80],
            'English': [75, 85, 82]}
    df=pd.DataFrame(data)
    # print(df)

    df_Math = df['Math']
    X_min = df_Math.min()
    X_max = df_Math.max()

    df_Math_scaled =(df_Math - X_min) / (X_max - X_min)
    print(df_Math_scaled)


if __name__== "__main__":
    main()