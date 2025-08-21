import random

n= random.randint(1,100)
a=-1
guesses=1

while(a !=n):
    a=int(input("guess the number: "))
    if(a>n):
        print("guess the smaller number")
        guesses +=1
    elif(a<n):
        print("guess the bigger number")
        guesses +=1

print(f"you guess the number {n} in {guesses}attempts \n thank you for playing.")