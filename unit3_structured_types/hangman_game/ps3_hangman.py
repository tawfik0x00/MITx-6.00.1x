# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

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

# after run this code will print first two lines
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    lenSecret = len(secretWord)
    lenLetters = 0
    for char in secretWord:
        if char in lettersGuessed:
            lenLetters += 1
    return lenSecret == lenLetters



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word = ''
    
    for char in secretWord:
        if char in lettersGuessed:
            word = word + str(char) + ' '
        else:
            word = word + '_ '

    return word


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
     # define alphabet as list to remove some elements
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    # joing letters to convert to lowercase
    letters = ''.join(lettersGuessed)
    # convert to lowercase
    letters = letters.lower()
    # loop throw letters and remove from a list of alphabet
    for letter in letters:
        if letter in alphabet:
          alphabet.remove(letter)
    
    # return a string of this list
    return str(''.join(alphabet))
    

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
    # FILL IN YOUR CODE HERE...
    # the length of the secret word
    secretWordLength = len(secretWord)

    # start the game and print welcome message
    print("Welcome to the game Hangman!")

    # print the len of the secret word
    print("I am thinking of a word that is", secretWordLength, "letters long")

    # start interact with the user
    numberOfGuesses = 8   

    lettersGuessed = []
    print("-----------")
    while numberOfGuesses > 0:
        # print a line of -- and number of guesses
       
        print("You have", numberOfGuesses,"guesses left")

        # print avalable letters
        availableLetters = getAvailableLetters(lettersGuessed)
        print("Available Letters: ", availableLetters)


        # get the letter and add it to lettersGuessed
        letter = input("Please guess a letter: ").strip()
        letter = letter[0]
        prevLetters = lettersGuessed[:]

        if letter in prevLetters and letter in secretWord:
          # get guessed word 
          print("Oops! You've already guessed that letter:", word)


        # add the letter to letterGuessed
        if letter not in lettersGuessed:
          lettersGuessed.append(letter)

        word = getGuessedWord(secretWord, lettersGuessed)

        if letter in secretWord:
          print("Good guess: ", word)
      
        
        if letter not in secretWord:
          print("Oops! That letter is not in my word:", word)


        print("------------")

        #check if is gueesed the word letters
        if isWordGuessed(secretWord, lettersGuessed):
          print("Congratulations, you won!")
          break

        if letter not in secretWord:
           numberOfGuesses -= 1
    
    if isWordGuessed(secretWord, lettersGuessed) == False:
      print("Sorry, you ran out of guesses. The word was", secretWord + ".")

# choose secret word
# secretWord = chooseWord(wordlist).lower()
hangman("sea")
