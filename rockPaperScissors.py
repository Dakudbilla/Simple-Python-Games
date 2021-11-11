#this does rock paper scissors game

import random

def play():
    user_score=0
    computer_score=0
    while True:
        user=input (" 'r' for rock \n 'p' for paper \n 's' for scissors \n What is your choice: ")
        if user!='r' and user!='s'  and user!='p' and user.lower()!='exit':
            print("Please Enter a valid value.")
            continue
        if(user.lower()=="exit"):
            break
        computer = random.choice(['r','p','s'])
        print(f"Your choice is : {user} \nComputer Choice is : {computer}\n")
       
        if user==computer:
             print('tie')
        elif is_win(user,computer):
            user_score=user_score+1
            print( "You Won!!!")
        else:
            computer_score=computer_score+1
            print( "You Lost :(")

        

    print(f"Your score is :{user_score} \n Computer score is: {computer_score}")

    

def is_win(player,opponent):
    #return true if player wins
    #r>s,s>p,p>r

    if(player=='r' and opponent=='s') or (player=='s' and opponent =='p')  or (player =='p' and opponent =='r'):
        return True

play()