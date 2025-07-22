# Q6:
# Sort the DataFrame by 'Total' marks in descending order 


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

    df_sort=df.sort_values(by='Total',ascending=False)
    print(df_sort)



if __name__=="__main__":
    main()