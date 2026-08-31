# Problem 5 - Playing a Hand

## Problem Statement

Implement `playHand(hand, wordList, n)` that allows a single human player to play through one hand of the word game. The hand ends when the player types `"."` to quit or runs out of letters.

**Sample interaction:**

```
Current Hand:  a c i h m m z
Enter word, or a "." to indicate that you are finished: him
"him" earned 24 points. Total: 24 points

Current Hand:  a c m z
Enter word, or a "." to indicate that you are finished: cam
"cam" earned 21 points. Total: 45 points

Current Hand:  z
Enter word, or a "." to indicate that you are finished: .
Goodbye! Total score: 45 points.
```

## Approach

Display the current hand, prompt the user for a word, and validate it with `isValidWord`. If valid, score it with `getWordScore` and update the hand with `updateHand`. If invalid, display an error and allow a retry. The loop ends when the user quits or the hand is empty.

This function is a building block for `playGame` in Problem 6 and the full game in [wordgame/](../wordgame/).

**Concepts practiced:**
- Building interactive game loops from helper functions
- Input validation and error handling
- Modular function composition
