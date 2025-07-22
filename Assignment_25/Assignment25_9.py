
# Q9:
# Replace values in 'Marks' less than 50 with 'Fail' using where(). 
# data = {'Marks': [45, 67, 88, 32, 76]} 

import pandas as pd 
import numpy as np 

def main():
    data = {'Marks': [45, 67, 88, 32, 76]} 
    df=pd.DataFrame(data)

    result_df = df.where(df['Marks'] > 50 ,"Fail")
    print(result_df)

if __name__=="__main__":
    main()     