import random
import string
from words import words

def get_valid_words(words):
    word= random.choice(words)
    while'-' in word or ' ' in word:
        word=random.choice(words)
    return word

def hangman():
    word=get_valid_words(words).upper()
    word_letters=set(word) #get all unique letters in word
    alphabet=set( string.ascii_uppercase) #contain user guesses
    used_letters=set() #what user has already guessed

    #get user inputs
    lives=len(word)+2
    while lives>0 and len(word_letters)>0:
        print(f"Lives left: {lives}")
        word_list=[]
         #letters used
        print('You have used these lettes: ',''.join(used_letters))

        #what current word is (ie W_RD)
        for letter in word:
            if letter.upper() in used_letters:
                word_list.append(letter)
            else:
                word_list.append('_')
                
        print('Current word: ',' '.join(word_list))
        user_letter= input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                
                word_letters.remove(user_letter)
            else:
                lives=lives-1

        elif user_letter in used_letters:
            
            print("You have already used this character, try again.")
        else:
            lives=lives-1
            print("Invalid character, try again.")


    if lives==0:
        print("You are dead :( the correct word is :",word)
    else:
        print(f"You WON!! you have succesfully guessed: {word}")    


hangman()