# MITx 6.00.1x — Introduction to Computer Science and Programming Using Python

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Course](https://img.shields.io/badge/Course-MITx-red)
![Status](https://img.shields.io/badge/Status-Completed-success)

This repository contains my personal solutions, projects, and completed exercises for MITx 6.00.1x: Introduction to Computer Science and Programming Using Python. This is an introductory computer science course offered by the Massachusetts Institute of Technology (MIT) on edX.

The course focuses on gaining confidence in Python programming, applying computation to solve problems, and understanding algorithmic complexity.

---

## What This Course Covers

MITx 6.00.1x builds a strong foundation in the following areas:

- Python Fundamentals: Syntax, variables, control flow, functions.
- Structured Data Types: Lists, tuples, dictionaries, strings, file I/O.
- Algorithmic Thinking: Recursion, searching and sorting algorithms, complexity analysis (Big O).
- Object-Oriented Programming (OOP): Classes, inheritance, encapsulation.
- Debugging and Testing: Assertions, exceptions, and defensive programming.

---

## Repository Structure

The repository is organized by units, corresponding to the core course topics and problem sets. Each unit directory contains a README with descriptions of every problem, and each problem directory contains its own README explaining the problem statement and approach.

### Unit 1 — Python Basics

Fundamental scripts addressing core syntax, variables, and string manipulation.

```
unit1_python_basics/
├── Problem_1/    # Count vowels in a string
├── Problem_2/    # Count occurrences of "bob" in a string
└── Problem_3/    # Find the longest alphabetically ordered substring
```

### Unit 2 — Simple Programs

Programs solving financial calculation tasks using control flow and function design, with increasing algorithmic efficiency.

```
unit2_simple_programs/
├── Problem_1/    # Remaining balance after minimum monthly payments
├── Problem_2/    # Minimum fixed monthly payment (exhaustive enumeration)
└── Problem_3/    # Minimum fixed monthly payment (bisection search)
```

### Unit 3 — Structured Types

Exercises demonstrating the use of lists, dictionaries, and string manipulation, culminating in a complete Hangman game.

```
unit3_structured_types/
├── Problem_1/    # isWordGuessed — check if word is fully guessed
├── Problem_2/    # getGuessedWord — build the partially revealed word
├── Problem_3/    # getAvailableLetters — list remaining letters
├── Problem_4/    # hangman — the full interactive game loop
└── hangman_game/ # Complete, runnable Hangman game
```

### Unit 4 — Good Programming Practices

Focus on writing modular, testable code. Seven problems incrementally build a Scrabble-inspired word game with both human and computer play modes.

```
unit4_good_programming_practices/
├── Problem_1/    # getWordScore — Scrabble-style word scoring
├── Problem_2/    # updateHand — remove played letters from hand
├── Problem_3/    # isValidWord — validate a word against hand and word list
├── Problem_4/    # calculateHandlen — count remaining letters in hand
├── Problem_5/    # playHand — play a single hand (human)
├── Problem_6/    # playGame — manage a multi-hand game (human only)
├── Problem_7/    # playGame — human vs. computer mode
└── wordgame/     # Complete, runnable word game (ps4a.py, ps4b.py)
```

### Unit 5 — Object-Oriented Programming

Advanced projects using OOP concepts. Four problems build a Caesar cipher system using a class hierarchy with inheritance.

```
unit5_object_oriented_programming/
├── Problem_1/    # Message class — shift dictionary and apply shift
├── Problem_2/    # PlaintextMessage — encrypt with a given shift
├── Problem_3/    # CiphertextMessage — brute-force decryption
├── Problem_4/    # decrypt_story — decrypt a real ciphered text file
├── Cipher/       # Complete, runnable Caesar cipher project
└── Cipher_Old/   # Earlier draft of the cipher (kept for reference)
```

---

## Key Projects

These directories contain the most substantial work in the course:

| Project | Unit | Description |
|---------|------|-------------|
| [Hangman Game](unit3_structured_types/hangman_game/) | Unit 3 | A fully functional command-line Hangman game with a 55,900-word dictionary |
| [Wordgame](unit4_good_programming_practices/wordgame/) | Unit 4 | A Scrabble-inspired word game with human and computer play modes, 83,667-word dictionary |
| [Cipher](unit5_object_oriented_programming/Cipher/) | Unit 5 | A Caesar cipher system that encrypts plaintext and automatically decrypts ciphertext |

---

## Skills Practiced

- Python Fundamentals: loops, conditionals, recursion
- Data Structures: lists, dictionaries, strings, tuples
- File I/O and string parsing
- Debugging and exception handling
- Modular and object-oriented design
- Algorithm design: exhaustive enumeration and bisection search
- Automated testing

---

## Academic Honesty

All solutions and code in this repository are my own work. They are intended solely for educational and archival purposes. If you are currently enrolled in this course, please do not copy these solutions, as it violates MITx and edX academic integrity policies.

---

## Author

Mohamed Tawfik
