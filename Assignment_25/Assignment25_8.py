# Q8:
# Fill missing values in a numeric column using interpolation. 

# data = {'Marks': [85, np.nan, 90, np.nan, 95]} 

import pandas as pd 
import numpy as np 

def main():
     data = {'Marks': [85, np.nan, 90, np.nan, 95]} 
     df=pd.DataFrame(data)
    
     df['Marks']=df['Marks'].fillna(df['Marks'].mean())
     print(df)

if __name__=="__main__":
    main()     


