# Vityarthi-Python-Project
# Unit Converter

Project title
Simple Unit Converter (Python)

Overview of the project
A small command-line Python script that converts between common units (length, mass, and temperature). The program prompts for a conversion choice and a numeric value, then prints the converted result.

Main script: [main.py](main.py)

Features
- Meter ↔ Kilometer
- Centimeter → Meter
- Gram ↔ Kilogram
- Celsius ↔ Fahrenheit
- Simple CLI input and output

Technologies / tools used
- Python 3 (recommended 3.8+)
- Terminal / Command Prompt

Files & key symbols
- [main.py](main.py)
  - Input choice variable: [main.c](main.py)
  - Input value variable: [main.v](main.py)
  - Output value variable: [main.result](main.py)

Steps to install & run the project
1. Install Python 3.8+ from https://www.python.org/ if not already installed.
2. Open a terminal in the project directory (where [main.py](main.py) is located).
3. Run:
sh
python main.py
Instructions for testing
- Manual test: run the script and enter the menu number and value when prompted.
- Example test cases:
  - Choice 1, value 1500 → expected output: 1500 meters = 1.5 kilometers
  - Choice 2, value 1.2 → expected output: 1.2 kilometers = 1200.0 meters
  - Choice 6, value 0 → expected output: 0 °C = 32.0 °F
  - Choice 7, value 32 → expected output: 32 °F = 0.0 °C
- For automated tests, create a small test harness that provides stdin values and asserts stdout contains expected strings.
 Notes & suggestions
- Add input validation to handle non-numeric input and out-of-range choices.
- Consider packaging conversion functions into callable functions for easier unit testing.
