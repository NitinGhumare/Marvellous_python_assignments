# Q7:
# Create a bar plot of student names vs total marks. 

import pandas as pd 
import matplotlib.pyplot as plt 
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

    ax = df[['Name','Total']].plot(kind='bar', title ="test", figsize=(15, 10), legend=True, fontsize=12)
    ax.set_xlabel("Name", fontsize=12)
    ax.set_ylabel("Total", fontsize=12)
    plt.show()



if __name__=="__main__":
    main()