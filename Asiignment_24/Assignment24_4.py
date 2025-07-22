# Q4: Plot a pie chart of subject marks for 'Sagar'. 


import pandas as pd
import matplotlib.pyplot as plt


def main():
    data= {'Name': ['Amit', 'Sagar', 'Pooja'],
            'Math': [85, 90, 78],
            'Science': [92, 88, 80],
            'English': [75, 85, 82]}
    df=pd.DataFrame(data)
    # print(df)

    df_sagar = df[df['Name']=='Sagar']
    sagar_score=df_sagar[['Math','Science','English']].iloc[0]
    plt.figure(figsize=(6, 6))
    plt.pie(sagar_score, labels=sagar_score.index, autopct='%1.1f%%', startangle=90)
    plt.title("Sagar's Subject Marks Distribution")
    plt.axis('equal')  # Equal aspect ratio to make it a circle
    plt.show()

if __name__== "__main__":
    main()