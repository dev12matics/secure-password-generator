# Secure Password Generator

A desktop password generator built with Python and Tkinter.

## Features

- Generates passwords from 4 to 50 characters
- Lets users include or exclude lowercase letters, uppercase letters, digits, and symbols
- Uses Python's `secrets` module for cryptographically secure random selection
- Validates user input and displays clear error messages
- Provides a read-only output field
- Copies generated passwords directly to the system clipboard

## Tech

- Python
- Tkinter
- `secrets`

## Run

```bash
python password_generator.py
```

Tkinter is included with most standard Python installations.

## Security note

Password generation uses `secrets` rather than `random`, making it more appropriate for security-sensitive random values.

## What this project demonstrates

- Desktop GUI development
- Input validation
- Event-driven programming
- Secure random generation
- Clipboard integration
