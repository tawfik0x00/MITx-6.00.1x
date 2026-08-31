# Problem 2 - Counting Occurrences of "bob"

## Problem Statement

Given a string `s` of lowercase characters, write a program that counts and prints the number of times the substring `bob` appears in `s`.

**Example:**

```
Input:  azcbobobegghakl
Output: number of times "bob" occurs is: 2
```

## Approach

Use a sliding window of size 3. Loop from index `0` to `len(s) - 2` and at each step extract the 3-character slice `s[i:i+3]`. If the slice equals `'bob'`, increment the counter.

This approach correctly handles overlapping occurrences (e.g., `bobob` contains two instances of `bob`).

**Concepts practiced:**
- String slicing
- Loop indexing with `range`
- Substring matching
