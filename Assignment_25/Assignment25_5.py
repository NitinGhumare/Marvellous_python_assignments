# Q5:
# Create a DataFrame with 'Age' and 'Purchased' columns and split into train/test sets. 
# data = {'Age': [22, 25, 47, 52, 46, 56], 'Purchased': [0, 1, 1, 0, 1, 0]}
import pandas as pd 
from sklearn.model_selection import train_test_split 

def main():
    data = {'Age': [22, 25, 47, 52, 46, 56], 'Purchased': [0, 1, 1, 0, 1, 0]}
    df=pd.DataFrame(data) 

    x =df[['Age']]
    y=df['Purchased']

    x_train , x_test ,y_train ,y_test =train_test_split(x,y,test_size=0.2,random_state=42)

    print("Training set is X :  ",x_train)
    print("Testing set is : ",x_test)
    print("Training set is Y: ",y_train)
    print("Testing set is Y: ",y_test)

if __name__=="__main__":
    main()


