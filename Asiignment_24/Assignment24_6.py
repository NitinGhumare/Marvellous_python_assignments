# Q6: Count how many students passed.


import pandas as pd 

def main():
    data= {'Name': ['Amit', 'Sagar', 'Pooja'],
            'Math': [85, 90, 78],
            'Science': [92, 88, 80],
            'English': [75, 85, 82]}
    df=pd.DataFrame(data)
    # print(df)

    print("Adding new column to dataframe of Total")

    df['Total']=df[['Math','Science','English']].sum(axis=1)
    # print(df) 

    df['Status']= df.apply(lambda x: "Pass" if x['Total']>=250 else 'Fail',axis=1)
    # print(df) 
    print(df['Status'].value_counts())




if __name__=="__main__":
    main() 



   