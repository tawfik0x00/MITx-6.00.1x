# Cipher — Caesar Cipher Encryption & Decryption

A Python implementation of a Caesar cipher developed as part of MITx
6.00.1x: Introduction to Computer Science and Programming Using Python.

## Overview

This project implements a Caesar cipher system capable of encrypting and
decrypting messages using configurable alphabet shifts. It also includes
logic for identifying the most likely encryption shift when the shift is
unknown.

## Features

- Encrypt plaintext using a Caesar cipher
- Decrypt ciphertext using a specified shift
- Support for arbitrary alphabet shifts
- Preserve uppercase and lowercase characters
- Detect possible shifts using a word dictionary
- Object-oriented design using inheritance

## Architecture

The implementation is organized around:

- `Message` — base class for message processing
- `PlaintextMessage` — encryption and plaintext handling
- `CiphertextMessage` — ciphertext analysis and decryption

## Concepts Demonstrated

- Python
- Object-Oriented Programming
- Classes and inheritance
- String manipulation
- Dictionaries and lists
- Algorithms
- File processing
- Problem solving

## How It Works

The Caesar cipher shifts each alphabetic character by a fixed number of
positions while preserving the character's case.

For example:

```text
Plaintext:  HELLO
Shift:      3
Ciphertext: KHOOR
