def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    False otherwise
    '''
    lenSecret = len(secretWord)
    lenLetters = 0
    for char in secretWord:
        if char in lettersGuessed:
            lenLetters += 1
    return lenSecret == lenLetters
