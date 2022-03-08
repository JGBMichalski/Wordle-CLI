# Requires Python 3.10 - This is due to the `match` statement used in the `GetAttemptString` function
from random import randint
from Classes.Text import Colours

import re
import sys

MAX_ATTEMPTS   = 5 # Maximum number of attempts before you lose

CHAR_INCORRECT = '0' # Value used to signify if a character in the string is incorrect
CHAR_IN_WORD   = '1' # Value used to signify if a character in the string is in the word, but not in its current position
CHAR_MATCH     = '2' # Value used to signify if a character in the string is in the correct position

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # An array of every letter of the alphabet

def GetWord():
    """
    Gets the word from the file.
    """
    # Open the `words` file and read all the words
    with open("words", 'r') as file:
        words = file.readlines()

    # Return a random word in the file and remove whitespace and convert to uppercase
    return words[randint(0, len(words))].strip().upper()

def GetAttemptString(attempts):
    """
    Creates the string used to display the current attempt.
    """
    match attempts:
        case 1:
            return "1st"
        case 2:
            return "2nd"
        case 3:
            return "3rd"
        case _:
            return "{}th".format(attempts)

def CompareStrings(guess, word):
    """
    Compares the guessed string with the word and generates a character map that holds
    the results of each letter comparison.
    """
    result = ""

    # Check if the words are the same length and if they contain only letters. If not, just exit.
    if (len(guess) != len(word)) or (not re.search(re.compile('^[' + ALPHABET + "]+$"), guess)):
        return result
    
    # Iterate through every letter
    for pos in range(0, len(guess)):
        if (guess[pos] not in word):
            result += CHAR_INCORRECT
        elif (guess[pos] == word[pos]):
            result += CHAR_MATCH
        else:
            result += CHAR_IN_WORD
    
    return result

def ColourWord(word, characterMap):
    """
    Adds the appropriate colour to each letter. Will also pad the letters with a space.
    """
    result = ""

    # Iterate through every letter
    for pos in range(0, len(word)):
        if (characterMap[pos] == CHAR_MATCH):
            result += Colours.GREEN + word[pos] + Colours.END
        elif (characterMap[pos] == CHAR_IN_WORD):
            result += Colours.YELLOW + word[pos] + Colours.END
        else:
            result += word[pos]
        result += " "
    
    return result

def UpdateColourArray(word, characterMap, colourArray):
    """
    Updates the colour array with the updated guess. The colour array is used to highlight
    which letters have been used and which letters have yet to be used.
    """
    # Iterate through every letter
    for pos in range(0, len(word)):
        if (characterMap[pos] == CHAR_MATCH) or (characterMap[pos] == CHAR_IN_WORD) or (characterMap[pos] == CHAR_INCORRECT):
            letterIndex = ALPHABET.find(word[pos])
            colourArray[letterIndex] = Colours.DARK
    
    return colourArray

def AssembleColourAlphabetString(colourArray):
    """
    Assembles the printable string that highlights which letters have been used.
    """
    result = ""

    # Iterate through every letter
    for pos in range(0, len(colourArray)):
        result += colourArray[pos] + ALPHABET[pos] + " " + Colours.END
    
    return result

if __name__ == "__main__":
    """
    Program's main loop.
    """
    colourArray = [Colours.WHITE for pos in range(26)] # Initialize the Colour Array with the default WHITE colour
    attempts = 1 # How many attempts we have made
    word = GetWord() # The word we will attempt to guess

    while (True):
        # Request the user's input
        guess = input("\nEnter your {} attempt: ".format(GetAttemptString(attempts))).strip().upper()

        # Compare the strings and get the resulting character map (Ex: "01200" - See `CHAR_MATCH`, `CHAR_IN_WORD`, and `CHAR_INCORRECT`)
        characterMap = CompareStrings(guess, word)

        # Don't process anything if the characters entered are incorrect
        if (characterMap == ""):
            print("Invalid guess. The word must be 5 characters long and only contain letters.")
            continue

        # Print the result of the character map against the guessed word
        print(ColourWord(guess, characterMap))

        # Check if the user won
        if (CHAR_IN_WORD not in characterMap) and (CHAR_INCORRECT not in characterMap):
            sys.exit("\nYou guessed {} successfully in {} attempts!".format(word, attempts))

        attempts += 1 # Increase attempts

        # End the game if attempts has exceeded the maximum number of attempts
        if (attempts > MAX_ATTEMPTS):
            sys.exit("\nUh oh. You lost. The word was {}.".format(word))
        
        # Update the colour array to include the new letters guessed
        colourArray = UpdateColourArray(guess, characterMap, colourArray)

        # Print out the colour array
        print("Remaining letters:\n{}".format(AssembleColourAlphabetString(colourArray)))