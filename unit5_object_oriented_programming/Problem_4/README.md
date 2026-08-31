# Problem 4 - Decrypt a Story

## Problem Statement

Use the `CiphertextMessage` class to decrypt the contents of `story.txt`, a file containing a Caesar-ciphered story. Implement the function `decrypt_story()` that reads the encrypted story, determines the correct shift, and returns the decrypted text.

## Approach

Call `get_story_string()` (provided helper) to read the encrypted story. Pass the result to `CiphertextMessage`, then call `decrypt_message()` on it. The method automatically tries all 26 shifts and returns the best one. Return the tuple containing the shift and the decrypted text.

**Example usage:**

```python
shift, decrypted = decrypt_story()
print("Shift used:", shift)
print(decrypted)
```

The full cipher implementation is in [Cipher/](../Cipher/).

**Concepts practiced:**
- Applying a class-based system to a real problem
- File I/O via a helper function
- End-to-end use of the `Message` class hierarchy
