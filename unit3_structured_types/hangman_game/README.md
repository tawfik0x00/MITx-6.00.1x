# Hangman Game

A fully playable command-line implementation of the classic Hangman game, developed as the capstone project for Unit 3 of MITx 6.00.1x.

## Overview

The computer randomly selects a word from a large word list. The player guesses one letter at a time. Correct guesses reveal the letter in the word; incorrect guesses reduce the number of remaining guesses. The player wins by uncovering all letters before exhausting their 8 allowed guesses.

## Files

| File | Description |
|------|-------------|
| `hangman.py` | Main game implementation — the `hangman()` function and game entry point |
| `ps3_hangman.py` | Helper module provided by the course: loads the word list and defines `isWordGuessed`, `getGuessedWord`, and `getAvailableLetters` |
| `words.txt` | Dictionary of 55,900 English words used to randomly select the secret word |

## How to Run

```bash
python hangman.py
```

The game uses the secret word `"sea"` by default at the bottom of `hangman.py`. To play with a random word, replace the call at the bottom with:

```python
import random
from ps3_hangman import loadWords, chooseWord
wordList = loadWords()
hangman(chooseWord(wordList))
```

## Gameplay

```
Welcome to the game Hangman!
I am thinking of a word that is 3 letters long
-----------
You have 8 guesses left
Available Letters: abcdefghijklmnopqrstuvwxyz
Please guess a letter: s
Good guess:  s _ _
------------
You have 8 guesses left
Available Letters: abcdefghijklmnopqrtuvwxyz
...
```

## Architecture

The game is built around three helper functions that were developed incrementally in Problems 1-3 of Unit 3:

- `isWordGuessed(secretWord, lettersGuessed)` — checks if the word has been fully guessed
- `getGuessedWord(secretWord, lettersGuessed)` — returns the partially revealed word
- `getAvailableLetters(lettersGuessed)` — returns remaining unguessed letters

The `hangman()` function in `hangman.py` imports these from `ps3_hangman` and ties them together into the interactive game loop.

**Concepts demonstrated:**
- Modular design with helper functions
- Interactive game loops
- List and string manipulation
- Random word selection from a file
