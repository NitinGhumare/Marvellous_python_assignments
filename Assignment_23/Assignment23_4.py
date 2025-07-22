# Q4:
# Display students who scored more than 85 in Science.

import pandas as pd 

def main():
    data= {'Name': ['Amit', 'Sagar', 'Pooja'],
            'Math': [85, 90, 78],
            'Science': [92, 88, 80],
            'English': [75, 85, 82]}
    df=pd.DataFrame(data)
    print(df)

    print("Students who scored more than 85 in Science ")

    df_result = df[df['Science'] > 85]
    print(df_result)



if __name__=="__main__":
    main()