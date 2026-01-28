def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    
        

    if word in wordList:

        hand_copy = hand.copy()

        for letter in word:

            if letter not in hand_copy:
                return False
            elif letter in hand_copy.keys():
                if hand_copy[letter] == 0:
                    return False
                else:
                    hand_copy[letter] -= 1

        return True
    
    return False