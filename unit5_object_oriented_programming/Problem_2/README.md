# Problem 2 - PlaintextMessage

## Problem Statement

Implement the `PlaintextMessage` class, a subclass of `Message`, that encrypts a given message using a specified shift value and exposes the result through getter methods.

**Methods to implement:**
- `__init__(self, text, shift)` — initialize using the parent class constructor, then store the shift and pre-compute the encrypted message.
- `get_shift(self)` — return the shift value.
- `get_encrypting_dict(self)` — return a copy of the shift dictionary to prevent mutation.
- `get_message_text_encrypted(self)` — return the encrypted text.
- `change_shift(self, shift)` — update the shift and re-encrypt the message.

## Approach

Call `Message.__init__` from the subclass constructor. Use `build_shift_dict` and `apply_shift` inherited from the parent to compute and store the encrypted text. `change_shift` simply re-runs the same initialization logic with the new shift value.

This class is used in the Cipher project at [Cipher/](../Cipher/).

**Concepts practiced:**
- Class inheritance and calling parent constructors with `super()` or explicit calls
- Encapsulation — exposing state through getter methods
- Defensive copying to prevent external mutation
