# Secure Password Generator

A beginner-friendly desktop password generator built with Python and Tkinter.

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

## Run

```bash
python password_generator.py
```

## What I learned

- Building a GUI with Tkinter
- Using `BooleanVar` and `StringVar`
- Connecting buttons to callback functions
- Input validation with `try` / `except`
- Working with Python's `string` and `secrets` modules
- Reading and updating GUI state
- Using the system clipboard from Tkinter

## Security note

This project uses Python's `secrets` module rather than `random` for password generation.
