def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    hand = None
    while True:
        choice = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ").strip().lower()[0]
        if choice in "nre":

            if choice == "e":
                return None
            elif choice == "n":

                # create a hand to play with it
                n = HAND_SIZE
                hand = dealHand(n)

                while True:

                    secondChoice = input("Enter u to have yourself play, c to have the computer play: ").strip().lower()[0]
                    if secondChoice in "uc":
                        if secondChoice == "u":
                            playHand(hand, wordList,  n)
                            break
                        elif secondChoice == "c":
                            compPlayHand(hand, wordList, n)
                            break
                    else:
                        print("Invalid command.")
                        print()

                # check the player the user or the computer and start playing
            elif choice == "r":
                # check if the user played before if not 
                if hand is None:
                    print("You have not played a hand yet. Please play a new hand first!")
                    print()
                else:
                    while True:
                        secondChoice = input("Enter u to have yourself play, c to have the computer play: ").strip().lower()[0]
                        if secondChoice in "uc":
                            if secondChoice == "u":
                                playHand(hand, wordList, n)
                                break
                            elif secondChoice == "c":
                                compPlayHand(hand, wordList, n)
                                break
                        else:
                            print("Invalid command.")
                            print()
        else:
            print("Invalid command.")
            print()
