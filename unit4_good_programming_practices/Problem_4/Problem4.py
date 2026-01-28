def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    
    handlen = 0
    for key in hand:
        if hand[key] != 0:
            handlen += hand[key]

    return handlen
