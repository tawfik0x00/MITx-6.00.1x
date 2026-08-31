# Problem 3 - Valid Words

## Problem Statement

Implement the function `isValidWord(word, hand, wordList)` that returns `True` if a word is both in the word list and can be formed using the letters currently in the hand.

**Validity conditions:**
1. The word must appear in `wordList`.
2. Every letter in the word must be available in sufficient quantity in the hand.

## Approach

First, check if the word exists in the word list. Then, use `getFrequencyDict` to get the letter frequencies in the word, and compare each letter's required count against its available count in the hand using `hand.get(letter, 0)`. If any letter is insufficient, return `False`.

This is a helper function for the Wordgame project in [wordgame/](../wordgame/).

**Concepts practiced:**
- Dictionary-based frequency comparison
- Short-circuit logic (early return on invalid condition)
- Composing helper functions (`getFrequencyDict`)
