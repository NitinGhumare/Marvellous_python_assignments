# Q8: Plot a histogram of math marks.
import pandas as pd 
import matplotlib.pyplot as plt 
def main():
    data= {'Name': ['Amit', 'Sagar', 'Pooja'],
            'Math': [85, 90, 78],
            'Science': [92, 88, 80],
            'English': [75, 85, 82]}
    df=pd.DataFrame(data)
    # print(df)

    plt.hist(df['Math'], bins=5)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title("Histogram of Math") 
    plt.show()

if __name__=="__main__":
    main()