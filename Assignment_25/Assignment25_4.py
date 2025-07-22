
# Q4:
# Apply One-Hot Encoding to a 'Department' column.
# data = {'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']}
import pandas as pd 
from sklearn.preprocessing import OneHotEncoder
def main():
    data = {'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']}
    df=pd.DataFrame(data)

    X =OneHotEncoder()
    df['Department']=X.fit_transform(df['Department'])
    print(df)



if __name__=="__main__":
    main()  