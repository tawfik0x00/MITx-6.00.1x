# Problem 2 - Dealing with Hands (updateHand)

## Problem Statement

Implement the function `updateHand(hand, word)` that removes from the hand the letters used to spell a given word, and returns the updated hand as a new dictionary without mutating the original.

**Example:**

```python
hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
updateHand(hand, 'quail')
# Returns: {'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
```

## Background

In this word game, a hand is a dictionary where keys are letters and values are the count of that letter available. This function models the action of playing a word — used letters are deducted from the hand.

## Approach

Copy the hand dictionary to avoid mutating the original. For each letter in the word, decrement its count in the copy by 1. Return the modified copy.

This is a helper function for the Wordgame project in [wordgame/](../wordgame/).

**Concepts practiced:**
- Dictionary mutation vs. copying
- Iterating over string characters to update a dictionary
- Defensive programming (no side effects)
