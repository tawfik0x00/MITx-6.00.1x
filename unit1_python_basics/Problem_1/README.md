# Problem 1 - Counting Vowels

## Problem Statement

Given a string `s` of lowercase characters, write a program that counts and prints the number of vowels in the string.

Valid vowels are: `a`, `e`, `i`, `o`, `u`.

**Example:**

```
Input:  azcbobobegghakl
Output: Number of vowels: 5
```

## Approach

Iterate over each character in the string with a `for` loop. For each character, check whether it belongs to the set of vowels. Maintain a counter that increments on each match, then print the final count.

**Concepts practiced:**
- String iteration
- Membership testing with `in`
- Counter variables
