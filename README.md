# Secure Password Generator

A desktop password generator built with Python and Tkinter.

## Features

- Generate passwords from 4 to 50 characters
- Optional lowercase letters
- Optional uppercase letters
- Optional digits
- Optional symbols
- Uses Python's `secrets` module for secure random selection
- Input validation with Tkinter error dialogs
- Read-only password output field
- Copy generated passwords to the system clipboard

## Requirements

- Python 3
- Tkinter (included with most standard Python installations)

## Usage

```bash
python password_generator.py
```

## Security

Password generation uses Python's `secrets` module rather than `random`.
