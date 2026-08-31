# Problem 7 - Human vs. Computer Word Game

## Problem Statement

Extend `playGame(wordList)` so that each hand can be played either by the human or by the computer. The computer uses `compChooseWord` to automatically select the highest-scoring valid word it can find in the hand.

**Menu commands (outer loop):**
- `n` — deal a new hand
- `r` — replay the last hand
- `e` — end the game

**Menu commands (inner prompt, once a hand is dealt):**
- `u` — human plays the hand
- `c` — computer plays the hand

**Sample interaction:**

```
Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: u
Current Hand: a s r e t t t
...

Enter n to deal a new hand, r to replay the last hand, or e to end game: r

Enter u to have yourself play, c to have the computer play: c
Current Hand:  a s r e t t t
"stretta" earned 99 points. Total: 99 points
```

## Approach

Reuse `playHand` for human play and `compPlayHand` for computer play. The key addition is prompting the player at the start of each hand to choose who plays. The rest of the multi-round game management logic from Problem 6 is preserved.

The full runnable game is in [wordgame/](../wordgame/).

**Concepts practiced:**
- Extending existing programs with new features
- Abstracting human and computer play behind the same interface
- Modular design for testability and flexibility
