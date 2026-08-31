# Problem 1 - Build the Shift Dictionary and Apply Shift

## Problem Statement

Implement two methods on the `Message` class that form the foundation of the Caesar cipher system:

1. `build_shift_dict(self, shift)` — builds a dictionary mapping each letter to its shifted counterpart. Both lowercase and uppercase letters are mapped, while punctuation, spaces, and digits are left unchanged.

2. `apply_shift(self, shift)` — applies the shift dictionary to the message text, returning the encrypted (or decrypted) string.

**Example:**

```
Original:  HELLO
Shift:     3
Ciphertext: KHOOR
```

## Approach

For `build_shift_dict`: iterate over `string.ascii_lowercase` and `string.ascii_uppercase`. For each letter at index `i`, the shifted letter is at index `(i + shift) % 26` in the same case alphabet. Store both mappings in the dictionary.

For `apply_shift`: iterate over each character in the message. If the character is in the shift dictionary, replace it; otherwise leave it unchanged. Join and return the result.

This is the base class used by `PlaintextMessage` (Problem 2) and `CiphertextMessage` (Problem 3). The full project is in [Cipher/](../Cipher/).

**Concepts practiced:**
- Object-oriented programming — class methods
- String module usage (`ascii_lowercase`, `ascii_uppercase`)
- Dictionary construction with modular arithmetic
