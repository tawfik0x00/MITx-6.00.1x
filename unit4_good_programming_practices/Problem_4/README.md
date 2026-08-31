# Problem 4 - Hand Length

## Problem Statement

Implement the helper function `calculateHandlen(hand)` that returns the total number of letters remaining in the hand.

**Example:**

```python
hand = {'a':1, 'q':1, 'l':1, 'm':1}
calculateHandlen(hand)  # Returns: 4
```

## Approach

Sum the values in the hand dictionary. Each value represents how many times that letter is available, so the sum gives the total remaining letters.

This is a prerequisite for implementing `playHand`, which needs to know when the hand is empty. Used in the Wordgame project in [wordgame/](../wordgame/).

**Concepts practiced:**
- Dictionary value aggregation
- Using `sum()` with dictionary values
