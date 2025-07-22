# Q7: Export the final DataFrame to a CSV file. 



import pandas as pd 

def main():
    data= {'Name': ['Amit', 'Sagar', 'Pooja'],
            'Math': [85, 90, 78],
            'Science': [92, 88, 80],
            'English': [75, 85, 82]}
    df=pd.DataFrame(data)
    # print(df)

    # print("Adding new column to dataframe of Total")

    df['Total']=df[['Math','Science','English']].sum(axis=1)
    # print(df) 

    df['Status']= df.apply(lambda x: "Pass" if x['Total']>=250 else 'Fail',axis=1)
    # print(df) 
    
    df.to_csv("FinalDf.csv")




if __name__=="__main__":
    main() 
