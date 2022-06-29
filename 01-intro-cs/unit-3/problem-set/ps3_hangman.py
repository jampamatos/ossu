# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    return set(secretWord) <= set(lettersGuessed)



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    return ''.join([' _ ' if l not in lettersGuessed else l for l in secretWord])



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    return ''.join(sorted(set(string.ascii_lowercase) - set(lettersGuessed)))



def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    wordLength = len(secretWord)
    guessesLeft = 8
    lettersGuessed = []
    
    print('Welcome to the game of Hang the Coder!')
    print('I am thinking of a word that is', wordLength, 'letters long.')
    print('-------------')
    
    while guessesLeft > 0:
      print('You have', guessesLeft, 'guesses left.')
      print('Available letters:', getAvailableLetters(lettersGuessed))
      letter = str.lower(input('Please guess a letter: '))
      
      if len(letter) > 1:
        print('Please, type only one letter.')
        print('-------------')
      else:
        
        if letter not in lettersGuessed:
          lettersGuessed += letter
          if letter in secretWord:
            print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
          else:
            print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
            guessesLeft -= 1
        else:
          print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
          print('-------------')
        
        if isWordGuessed(secretWord, lettersGuessed):
          print('Congratulations, you won!')
          exit()
      
    print('Sorry, you ran out of guesses. The word was', secretWord + '.')
        






secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
