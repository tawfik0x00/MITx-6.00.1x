# Problem 4 - The Hangman Game Loop

## Problem Statement

Implement the `hangman(secretWord)` function that runs a complete interactive Hangman game between the user and the computer. This function ties together all three helper functions from Problems 1, 2, and 3.

**Game rules:**
- The player starts with 8 guesses.
- Each incorrect guess costs one guess.
- Guessing a letter already guessed does not cost a guess but shows a reminder.
- The game ends when the word is fully guessed (win) or all guesses are exhausted (loss).
- On loss, the secret word is revealed.

## Approach

Maintain a list of guessed letters and a guess counter. On each turn, print the remaining guesses and available letters, then prompt the user for input. Check whether the letter was already guessed, whether it is in the word, and update state accordingly. After each turn, check for a win condition using `isWordGuessed`. After the loop, check for the loss condition and print the secret word if applicable.

The complete, playable game is located in [hangman_game/](../hangman_game/).

**Concepts practiced:**
- Game loop design with while loops
- Composing helper functions into a larger program
- Interactive I/O and input validation
- State management across loop iterations
