# Problem 3 - Longest Alphabetically Ordered Substring

## Problem Statement

Given a string `s` of lowercase characters, find and print the longest substring in which the letters appear in alphabetical (non-decreasing) order. In case of a tie, print the first such substring.

**Examples:**

```
Input:  azcbobobegghakl
Output: beggh

Input:  abcbcd
Output: abc
```

## Approach

Maintain two variables: `current` (the substring being built) and `longest` (the longest found so far). Iterate over the string starting from index 1. If the current character is greater than or equal to the previous character, extend `current`. Otherwise, compare `current` to `longest` and update if longer, then reset `current` to the new character.

After the loop, perform a final comparison to account for the case where the longest substring runs to the end of the string.

**Concepts practiced:**
- String traversal with index access
- Tracking state across iterations
- Character comparison using lexicographic ordering
