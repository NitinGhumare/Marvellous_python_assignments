# Q9:
# Create a DataFrame with missing values and fill them with column mean.

# data2 = {
#     'Name': ['Amit', 'Sagar', 'Pooja'],
#     'Math': [np.nan, 76, 88],
#     'Science': [91, np.nan, 85]
# }

import pandas as pd 
import numpy as np

def main():
    data= {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [np.nan, 76, 88],
    'Science': [91, np.nan, 85]}

    df=pd.DataFrame(data)
    # print(df) 
    numeric_cols = df.select_dtypes(include='number').columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    print(df)

if __name__=="__main__":
    main()    