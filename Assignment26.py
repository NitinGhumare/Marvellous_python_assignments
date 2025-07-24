import pandas as pd 
import numpy as np 
from sklearn.metrics import accuracy_score ,confusion_matrix
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder


def PlayPredictor(Datapath):
    df=pd.read_csv(Datapath)
    # print(df.head()) 

    df=df.drop(columns=['Unnamed: 0'])
    # print(df.head()) 
    print("Dimenstion of dataframe",df.shape) 

    LE = LabelEncoder()

    for col in df.columns:
        df[col]=LE.fit_transform(df[col])

    print(df.head())   

    x= df.drop(columns=['Play'])
    y = df['Play']


    def CheckAccuracy():
        for k in range (1,11):
               
               X_train, X_test, Y_train, Y_test = train_test_split(x,y,test_size=0.5,random_state=42)

               model = KNeighborsClassifier(n_neighbors=k)
 
               model.fit(X_train,Y_train)

               y_pred = model.predict(X_test) 

               Accuracy = accuracy_score(Y_test,y_pred)

               print(f"Accuracy for K={k}: {Accuracy:.2f}") 

    CheckAccuracy()                      



def main():
    PlayPredictor("PlayPredictor.csv") 


if __name__=="__main__":
    main()        
