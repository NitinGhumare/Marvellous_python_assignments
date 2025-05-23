# Accept a single character from the user and check if it is a vowel (a, e, i, o, u).
# If not, print it's a consonant

# Enter a character: e  

# 'e' is a vowel.  

vowel = "aeiou" 

def CheckVowel(n):
        
        if n in vowel:
             print('Chracter is vowel')

        else:
            print("character is not vowel")

if  __name__=="__main__":
    n=input("enter chracteer : ")


    CheckVowel(n)   

                    

       

        




