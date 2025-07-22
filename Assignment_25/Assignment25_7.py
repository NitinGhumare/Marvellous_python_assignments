# Q7:
# Normalize 'Age' column using Min-Max Scaling. 
# data = {'Age': [18, 22, 25, 30, 35]}
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np 

def main(): 
    data = {'Age': [18, 22, 25, 30, 35]} 
    df=pd.DataFrame(data)

    scaler = MinMaxScaler() 
    scaled_values = scaler.fit_transform(df) 
    
    df_scaled = pd.DataFrame(scaled_values, columns=df.columns)
    
    print(df_scaled)

if __name__=="__main__":
    main()    