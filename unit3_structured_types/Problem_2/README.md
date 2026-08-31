# Problem 2 - Getting the Guessed Word

## Problem Statement

Implement the function `getGuessedWord(secretWord, lettersGuessed)`. It returns a string showing which letters of the secret word have been guessed so far. Correctly guessed letters appear in their positions; unguessed letters are shown as `_ `.

**Example:**

```python
secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
getGuessedWord(secretWord, lettersGuessed)  # Returns: '_ pp_ e '
```

## Approach

Build an output string by iterating over each character in `secretWord`. If the character is in `lettersGuessed`, append the character followed by a space. Otherwise, append `_ ` (underscore with a space for readability). Return the final string.

This is a helper function used by the full Hangman game in [hangman_game](../hangman_game/).

**Concepts practiced:**
- String building with concatenation
- Conditional logic inside loops
- User-facing output formatting
