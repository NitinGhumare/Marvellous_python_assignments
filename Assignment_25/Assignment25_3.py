# Apply Label Encoding to a 'City' column.
# data = {'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi']}
import pandas as pd 
from sklearn.preprocessing import LabelEncoder
def main():
    data = {'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi']}
    df=pd.DataFrame(data)

    X =LabelEncoder()
    df['City']=X.fit_transform(df['City'])
    print(df)



if __name__=="__main__":
    main()    
