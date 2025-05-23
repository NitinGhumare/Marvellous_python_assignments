# Q3. Voting Eligibility Checker
# Task:
# Accept age from the user and check whether the person is eligible to vote.
# (Age should be 18 or above.)

def VotingCriteria(age):
    if age >= 18 :
        print("The persion is eligibale for voting")

    else:
        print("The person is not eligibale for voting")

if __name__=="__main__":
     age=int(input("Enter the age: "))

     VotingCriteria(age)            