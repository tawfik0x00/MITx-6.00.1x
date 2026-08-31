# Caesar Cipher

A Python implementation of a Caesar cipher encryption and decryption system, developed as the capstone project for Unit 5 of MITx 6.00.1x. This is the final, clean version of the implementation.

## Overview

The Caesar cipher shifts each letter in a message by a fixed number of positions in the alphabet. This project implements a full object-oriented cipher system that can encrypt a plaintext message with any shift, and decrypt a ciphertext message even when the shift is unknown — by trying all 26 possibilities and selecting the one that produces the most valid English words.

## Files

| File | Description |
|------|-------------|
| `ps6.py` | Main implementation — the `Message`, `PlaintextMessage`, and `CiphertextMessage` classes, plus `decrypt_story()` |
| `story.txt` | A Caesar-encrypted story used to test `decrypt_story()` |
| `words.txt` | Dictionary of valid English words used during decryption |

## How to Run

```bash
python ps6.py
```

The file includes example usage at the bottom to demonstrate encryption and decryption.

## Architecture

The system is built around a three-class hierarchy:

```
Message
  |
  +-- PlaintextMessage    (encrypts with a given shift)
  |
  +-- CiphertextMessage   (decrypts by trying all shifts)
```

### Message (base class)

- Stores the raw message text and the word list.
- `build_shift_dict(shift)` — builds a letter-to-letter mapping for the given shift.
- `apply_shift(shift)` — applies the mapping to produce encrypted or decrypted text.

### PlaintextMessage

- Stores the shift and the pre-computed encrypted text.
- `get_shift()`, `get_encrypting_dict()`, `get_message_text_encrypted()` — getters.
- `change_shift(shift)` — updates the shift and re-encrypts.

### CiphertextMessage

- `decrypt_message()` — tries all 26 shifts, counts valid English words for each, and returns `(best_shift, decrypted_text)`.

## Example

```python
plaintext = PlaintextMessage('Hello, World!', 5)
print(plaintext.get_message_text_encrypted())
# Output: Mjqqt, Btwqi!

ciphertext = CiphertextMessage('Mjqqt, Btwqi!')
print(ciphertext.decrypt_message())
# Output: (5, 'Hello, World!')
```

## Cipher Rules

- Uppercase and lowercase letters shift independently, preserving case.
- Spaces, punctuation, and digits are not shifted.
- Shifts wrap around: `z` shifted by 3 becomes `c`.

**Concepts demonstrated:**
- Object-oriented programming — classes, inheritance, encapsulation
- Brute-force decryption via exhaustive key-space search
- Modular arithmetic for circular alphabet shifting
- File I/O and word list validation
