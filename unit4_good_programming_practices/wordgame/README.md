# Wordgame

A Scrabble-inspired command-line word game developed as the capstone project for Unit 4 of MITx 6.00.1x. The game supports both human play and computer-automated play.

## Overview

Players are dealt a hand of random letters. On each turn, they form a valid English word using some or all of their letters, earning points based on Scrabble letter values multiplied by word length. A 50-point bonus is awarded for using all letters in a single word. Players can replay a hand or deal a new one. The computer opponent automatically selects the highest-scoring valid word from its hand.

## Files

| File | Description |
|------|-------------|
| `ps4a.py` | Part A — core game functions: scoring, hand management, validation, and human play |
| `ps4b.py` | Part B — computer play: `compChooseWord`, `compPlayHand`, and the extended `playGame` with human vs. computer mode |
| `test_ps4a.py` | Automated test suite for Part A functions |
| `words.txt` | Dictionary of 83,667 English words |
| `ProblemSet4.zip` | Original problem set archive from the course |

## How to Run

```bash
python ps4b.py
```

This launches the full game with both human and computer play modes.

To run the automated tests for Part A:

```bash
python test_ps4a.py
```

## Gameplay

```
Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: u

Current Hand: a s r e t t t
Enter word, or a "." to indicate that you are finished: tatters
"tatters" earned 99 points. Total: 99 points

Run out of letters. Total score: 99 points.
```

## Scoring

| Component | Formula |
|-----------|---------|
| Base score | sum of Scrabble letter values * word length |
| Bonus | +50 points if all n hand letters are used |

## Architecture

The game is built incrementally across seven problems, each implementing one function that the next depends on:

1. `getWordScore` — score a word
2. `updateHand` — remove played letters from the hand
3. `isValidWord` — validate a word against the word list and hand
4. `calculateHandlen` — count remaining letters
5. `playHand` — run one hand of human play
6. `playGame` — manage multiple hands (human only)
7. `playGame` (extended) — human vs. computer mode

**Concepts demonstrated:**
- Modular design and incremental development
- Dictionary-based data structures for hand representation
- Automated testing with `test_ps4a.py`
- Computer player using exhaustive word selection
