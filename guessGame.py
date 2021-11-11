##Computer generates a random number and 
##player guesses it

import random

def user_guess(x):
    random_num= random.randint(1,x)
    guess=0
    while guess !=random_num:
        guess=int( input(f"Guess a number between 1 and {x}: "))
        
        if guess<random_num:
            print("Sorry, Guess again, Too low")
        elif guess>random_num:
            print("Sorry, Guess again, too high")
    print(f"Aboozigi, Congratulations, You guessed {random_num} correctly")


#computer gets to guess my number
def computer_guess():
    user_num= int(input( "Please Enter a number for computer to Guess: "))
    low =1
    high=user_num
    feedback=''
    while True :
        guess = random.randint(low,high)
        if guess==user_num:
            break
        feedback=input(f"Is {guess} too high(H) or too low(L)".lower())
        
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
        else:
            print("Please Enter a valid input")
            continue
    print(f"Computer, You Guessed my number {user_num} right")

computer_guess()


