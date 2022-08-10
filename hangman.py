import random
import string
from words import words

def getValidWords(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    
    return word.upper()


def hangman():
    word = getValidWords(words)
    wordLetters = set(word) 
    alphabet = set(string.ascii_uppercase)
    usedLetters = set()

    lives = 6

    while len(wordLetters) > 0 and lives  > 0:
        print ("You have", lives, "lives left and you have used these letters: ", " ".join(usedLetters))

        

        wordList = [letter if letter in usedLetters else "-" for letter in word]
        print("Current word: ", " " .join(wordList))
   

        userLetter = input("Guess a letter: ").upper()
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)

            else:
                lives = lives - 1
                print("\n The letter," , userLetter, "is not in the chosen word try again.")


        elif userLetter in usedLetters:
            print("Letter previously used, Try a different letter.")

        else:
            print("Invalid character, please use a letter from the alphabet.")
    if lives == 0:
        print("You lose! You have run out of lives! The word was", word)
    else:
        print ("Congratulations! You guessed the correct word", word, "!")


if __name__ == '__main__':
    hangman()