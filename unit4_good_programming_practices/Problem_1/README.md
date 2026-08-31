# Problem 1 - Word Scores

## Problem Statement

Implement the function `getWordScore(word, n)` that returns the integer Scrabble-style score for a given word.

**Scoring rules:**
- Each letter is worth its Scrabble point value (e.g., A=1, B=3, C=3, D=2, ...).
- The word's base score is the sum of letter values multiplied by the word's length.
- If all `n` letters in the hand are used, add a 50-point bonus.

**Example:**

```
'weed' with n=7  ->  (4+1+1+2) * 4 = 32 points
'waybill' with n=7  ->  (4+1+4+3+1+1+1) * 7 + 50 = 155 points
```

## Approach

Sum the Scrabble point values for each character in the word using the `SCRABBLE_LETTER_VALUES` dictionary. Multiply the sum by the length of the word. If the word uses all `n` letters, add 50 bonus points.

This is a helper function for the Wordgame project in [wordgame/](../wordgame/).

**Concepts practiced:**
- Dictionary lookups
- Accumulator pattern
- Conditional bonus logic
