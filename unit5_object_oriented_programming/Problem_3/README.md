# Problem 3 - CiphertextMessage

## Problem Statement

Implement the `CiphertextMessage` class, a subclass of `Message`, that decrypts a Caesar-ciphered message by trying all 26 possible shifts and selecting the one that produces the most valid English words.

**Methods to implement:**
- `__init__(self, text)` — initialize using the parent class constructor.
- `decrypt_message(self)` — try all shifts from 0 to 25, count valid English words for each decryption, and return a tuple `(best_shift, decrypted_text)`.

## Approach

For each shift value (0 to 25), apply `apply_shift(26 - shift)` to reverse the encryption. Split the resulting text into words and count how many are valid using `is_word`. Track the shift that yields the maximum valid word count and return that shift along with the corresponding decrypted text.

This class is used in the Cipher project at [Cipher/](../Cipher/) and applied in Problem 4 to decrypt a real story.

**Concepts practiced:**
- Brute-force decryption by exhaustive search over a small key space
- Frequency analysis via word counting
- Tuple return values
- Inheritance — building on `Message` and `PlaintextMessage`
