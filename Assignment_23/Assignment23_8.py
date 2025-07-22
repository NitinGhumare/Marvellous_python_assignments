# Q8:
# Plot a line chart of marks for 'Amit' across all subjects. 


import pandas as pd 
import matplotlib.pyplot as plt

def main():
    data= {'Name': ['Amit', 'Sagar', 'Pooja'],
            'Math': [85, 90, 78],
            'Science': [92, 88, 80],
            'English': [75, 85, 82]}
    df=pd.DataFrame(data)
    print(df) 

    amit_index = df[df['Name'] == 'Amit'].index[0]

    
    marks = df.loc[amit_index, ['Math', 'Science', 'English']]

    
    marks.plot(kind='line', marker='o', title="Amit's Marks")
    plt.ylabel("Marks")
    plt.xlabel("Subjects")
    plt.grid(True)
    plt.show()

if __name__=="__main__":
    main()