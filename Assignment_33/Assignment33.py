import pandas as pd 
import numpy as np  
from sklearn.preprocessing import StandardScaler 
from sklearn.cluster import KMeans


def StudPerf(datapath):
    df= pd.read_csv(datapath,sep=';') 
    print(df.shape) 
    print(df.head())
    print(df.isna().sum()) 

    features = ['G1','G2','G3','studytime','failures','absences']
    X = df[features] 
    print(X) 

    scaler = StandardScaler() 
    X_scaled = scaler.fit_transform(X)
    print(X_scaled) 


    Cluster = KMeans(n_clusters=3,random_state=42) 
    df['Cluster'] =Cluster.fit_predict(X_scaled) 

    print(df['Cluster'])


    # Analyze cluster profiles
    cluster_profiles = df.groupby('Cluster')[features].mean()
    print("\nCluster Profiles:\n", cluster_profiles) 









def main(): 
    StudPerf("student-mat.csv")


if __name__=="__main__":
    main()    

