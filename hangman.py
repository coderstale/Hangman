import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 5

    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives left and You have used these letters: ", " ".join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word: ', ' '.join(word_list))
        user_letter = input("Guess the word: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives -= 1
                print("Letter is not in word!")

        elif user_letter in used_letters:
            print("You have already used that letter!")

        else:
            print("Invalid letter, please try again!")
    if lives == 0:
        print("Sorry. You died!, the word was", word)
    else:
        print("You guessed the word", word, '!!')


hangman()
