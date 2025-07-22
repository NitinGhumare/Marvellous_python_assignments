# Q2:
# Detect column data types and convert 'Age' from float to int.

# data = {'Name': ['A', 'B', 'C'], 'Age': [21.0, 22.0, 23.0]} 
import pandas as pd 

def main():
    data = {'Name': ['A', 'B', 'C'], 'Age': [21.0, 22.0, 23.0]}

    df = pd.DataFrame(data)
    print(df)
    print(df.info()) 

    df['Age']=df['Age'].astype(int)
    print(df.info())
if __name__=="__main__":
    main()    
