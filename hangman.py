import random
from words import words 
import string

# print(words)

def get_word(words):
    word = random.choice(words)
    while '-' in words or ' ' in words:
        word = random.choice(word)
    
    return word.upper()

def hangman():
    word = get_word(words)
    word_letters = set(word) 
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives>0:

        # ' '.join(['a','b','cd']) --> 'a b cd'
        print('you have', lives, 'lives left and you have used these letters:', ' '.join(used_letters))

        # what current word is (like -- w - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word_letters]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else:
                lives-=1
                print('Letter in sont in the word')
        
        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
        else:
            print('Invalid character. Please try again.')
    
    if lives == 0:
        print('Sorry you died. The word was', word)
    else:
        print('You guessed the word', word, '!!')

if __name__ == '__main__':
    hangman()