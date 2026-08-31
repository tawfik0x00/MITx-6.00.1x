# Problem 6 - Playing a Full Game (Human Only)

## Problem Statement

Implement `playGame(wordList)` that manages multiple rounds of the word game. The player can deal a new hand, replay the last hand, or end the game.

**Menu commands:**
- `n` — deal a new hand
- `r` — replay the last hand
- `e` — end the game

**Sample interaction:**

```
Enter n to deal a new hand, r to replay the last hand, or e to end game: r
You have not played a hand yet. Please play a new hand first!

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: p z u t t t o
...
```

## Approach

Maintain the current hand across iterations. On `n`, deal a new hand and play it. On `r`, replay the stored hand from the beginning. On `e`, exit. Handle invalid input by notifying the user.

The full runnable game is in [wordgame/](../wordgame/).

**Concepts practiced:**
- Multi-round game management
- State persistence across iterations (replaying a hand)
- Command dispatch with conditional logic
