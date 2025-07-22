# Q6:
# Replace multiple values in a column using a dictionary. 
# data = {'Grade': ['A+', 'B', 'A', 'C', 'B+']}

import pandas as pd 

def main():
    data = {'Grade': ['A+', 'B', 'A', 'C', 'B+']} 
    df=pd.DataFrame(data)

    df =df['Grade'].replace({'A+':'Excellent','B':'Good','A':'Very Good','C':'Poor','B+':'Good'})
    print(df)

if __name__=="__main__":
    main()    

