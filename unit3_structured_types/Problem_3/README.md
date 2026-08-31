# Problem 3 - Printing Available Letters

## Problem Statement

Implement the function `getAvailableLetters(lettersGuessed)`. It returns a string of all lowercase English letters that have not yet been guessed, in alphabetical order.

**Example:**

```python
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
getAvailableLetters(lettersGuessed)  # Returns: 'abcdfghjlmnoqtuvwxyz'
```

## Approach

Use `string.ascii_lowercase` as the full alphabet. Build a result string containing only those letters that are not present in `lettersGuessed`. Because `ascii_lowercase` is already in alphabetical order, the output is automatically sorted.

This is a helper function used by the full Hangman game in [hangman_game](../hangman_game/).

**Concepts practiced:**
- Standard library usage (`string` module)
- Set-difference logic via string filtering
- Producing alphabetically ordered output
