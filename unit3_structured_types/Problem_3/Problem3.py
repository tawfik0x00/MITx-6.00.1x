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
        alphabet.remove(letter)
    
    # return a string of this list
    return str(''.join(alphabet))