import random
import string
from words import words

# Function used for filtering out hyphonated words or words with spaces.
# Mainly because I just grabbed all the words from a random file with a bunch of english words in it.

def getValidWords(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    
    return word.upper()


def hangman():
    word = getValidWords(words)                     # Selects the word.
    wordLetters = set(word)                         # All the letters in the word.
    alphabet = set(string.ascii_uppercase)
    usedLetters = set()                             # The letters the user has guessed.

    lives = 6                                       # Sets the amount of lives.

    while len(wordLetters) > 0 and lives  > 0:
        print ("You have", lives, "lives left and you have used these letters: ", " ".join(usedLetters))

        # This removes the commas inbetween letters,
        # improving the playability of the game.         

        wordList = [letter if letter in usedLetters else "-" for letter in word]
        print("Current word: ", " " .join(wordList))
   
        # Takes in the user input eg "A"
        # Then uses an if statement to check if the letter is 
        # in the word and if it is, shows where in the word it is
        # and if it isn't deducts a life, and informs the user
        # to guess another letter. 

        userLetter = input("Guess a letter: ").upper()
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)

            else:
                lives = lives - 1
                print("\n The letter," , userLetter, "is not in the chosen word try again.")

        # Some quality of life code, to inform the user
        # that they have already used that letter
        # and they should select another one. 

        elif userLetter in usedLetters:
            print("Letter previously used, Try a different letter.")

        else:
            print("Invalid character, please use a letter from the alphabet.")

        # If they guess incorrectly too many times
        # and run out of lives they lose. 
        # If they guess the word the game informs them they win.

    if lives == 0:
        print("You lose! You have run out of lives! The word was", word)
    else:
        print ("Congratulations! You guessed the correct word", word, "!")


if __name__ == '__main__':
    hangman()