from ps3_hangman import getAvailableLetters, getGuessedWord, isWordGuessed

def hangman(secretWord):
    
    # len of secretWord
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

        # print available letters
        availableLetters = getAvailableLetters(lettersGuessed)
        print("Available Letters: ", availableLetters)

        # get the letter and add it to lettersGuessed
        letter = input("Please guess a letter: ").strip().lower()
        letter = letter[0]

        if letter in lettersGuessed:
            # if letter found in lettersGuessed before print this message with the word
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        else:
            # add the guessed letter
            lettersGuessed.append(letter)

            # check if letter is correct if its correct don't subtract one of counter
            if letter in secretWord:
                print("Good guess: ", getGuessedWord(secretWord, lettersGuessed))
            else:
                print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
                numberOfGuesses -= 1

        print("------------")

        # check if the word is fully guessed
        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            break
    
    if isWordGuessed(secretWord, lettersGuessed) == False:
        print("Sorry, you ran out of guesses. The word was", secretWord + ".")


hangman("sea")