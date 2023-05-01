import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while ('-' in word or ' ' in word):
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words)
    word = word.upper()
    lives = 6
    word_letters = set(word)
    alphabet =  set(string.ascii_uppercase)
    used_letters = set()

    while(len(word_letters) > 0 and lives > 0) :
        print("You have", lives, "lives left and you have already picked: ", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current Word: ", ' '.join(word_list))
        user_letter =  input("\nGuess a letter: ").upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if (user_letter in word_letters):
                word_letters.remove(user_letter)
            else:
                lives = lives-1
                print(f"{user_letter} is not in the word")
        elif user_letter in used_letters:
            print("You have already used that letter dummy!")
        else:
            print ("Error, invalid character selected. Please select a valid letter from the alphabet that has not already been chosen")
   # print (f"You Guessed the Word {word}. Congrats!")
    if (lives != 0):
        print(f"You guessed the Word {word.lower()}. Congrats!")
    else:
        print(f"Ugh, you ran out of lives! The word was {word.lower()}. Better luck next time!")

hangman()
