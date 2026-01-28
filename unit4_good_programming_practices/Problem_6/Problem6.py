def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    # # TO DO ... <-- Remove this comment when you code this function
    # print("playGame not yet implemented.") # <-- Remove this line when you code the function
    hand = None

    while True:
        choice = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ").strip()[0]
        if choice not in "nre":
            print("Invalid command.")
            pass
        else:
            if choice == "n":
                n = HAND_SIZE
                hand = dealHand(n)
                playHand(hand, wordList, HAND_SIZE)

            elif choice == "r":
                if hand is None:
                    print("You have not played a hand yet. Please play a new hand first!")
                    print()
                else:
                    playHand(hand, wordList, n)
            elif choice == "e":
                break