import random
import string
from words import words

def getValidWords(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = getValidWords
    wordLetters = set(word) 
    alphabet = set(string.ascii_uppercase)
    usedLetters = set()

    lives = 6

    while len(wordLetters) > 0 and lives  > 0:
        print ("You have used these letters: ', ' ".join(usedLetters))

        wordList = [letter if letter in usedLetters else "-" for letter in word]
        print("Current word: ', ' ".join(wordList))

        userLetter = input("Guess a letter: ").upper()
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)

            else:
                lives = lives - 1
                print("Letter is not in the word.")

        elif userLetter in usedLetters:
            print("Letter previously used, Try a different letter.")

        else:
            print("Invalid character, please use a letter from the alphabet.")

userInput = input("Type Anything:")
print(userInput)