# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "c:/Users/User1/Desktop/mit/Intro-to-Computer-Science-and-Programming-Using-Python/Problem Sets/Problem Set 3/words.txt"

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
        
    for i in range(len(secretWord)):
      if secretWord[i] not in lettersGuessed:
        return False
        break
        
    

    return True
      
        


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    nio = secretWord
    for i in range(len(secretWord)):
      if secretWord[i] not in lettersGuessed:
        nio = nio.replace(secretWord[i], '_ ')

    return nio


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    nio = string.ascii_lowercase
    for i in range(len(string.ascii_lowercase)):
      if string.ascii_lowercase[i] in lettersGuessed:
        nio = nio.replace(string.ascii_lowercase[i], '')
    return nio


def hangman(secretWord):
    mistakesMade = 8
    lettersGuessed = []
    matt = '_ '
    print('Welcome to the game of Hangman!')
    print('I am thinking of a word that is ', len(secretWord), 'letters long')
    while mistakesMade >= 1 or isWordGuessed(secretWord, lettersGuessed) == False:
      print("-----------")
      print('You have', mistakesMade, 'guesses left')
      print('Available letters:', getAvailableLetters(lettersGuessed))
      chad = input('Please guess a letter:')
      chad.lower
      if str(chad) in secretWord:
        if str(chad) in lettersGuessed:
          print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        else:
          lettersGuessed.append(str(chad))
          print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
          if matt not in getGuessedWord(secretWord, lettersGuessed):
            print("-----------") 
            print('Congratulations, you won!')
            break
      elif str(chad) not in secretWord:
        print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
        mistakesMade -= 1
        if mistakesMade == 0: 
          print('-----------')
          print('Sorry, you ran out of guesses. The word was', secretWord,'.')
          break
      else: print('Oops! Try again')
      lettersGuessed.append(str(chad))


   
secretWord = chooseWord(wordlist).lower()


hangman(secretWord)

    

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
