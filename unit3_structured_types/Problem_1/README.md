# Problem 1 - Is the Word Guessed

## Problem Statement

Implement the function `isWordGuessed(secretWord, lettersGuessed)`. It returns `True` if every letter of `secretWord` is in the `lettersGuessed` list, and `False` otherwise.

**Example:**

```python
secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
isWordGuessed(secretWord, lettersGuessed)  # Returns: False
```

## Approach

Iterate over each character in `secretWord`. Count how many of those characters appear in `lettersGuessed`. Compare the count to the length of the secret word — if they are equal, all letters have been guessed.

This is a helper function used by the full Hangman game in [hangman_game](../hangman_game/).

**Concepts practiced:**
- List membership testing
- Counter-based boolean checks
- Function design for reuse
