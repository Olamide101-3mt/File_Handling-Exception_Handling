#File Read & Write Challenge – Week 4 Assignment 📂
📖 Overview

This project demonstrates file handling and error management in Python.
The program reads a text file provided by the user, processes its content, and writes a modified version to a new file. It also handles errors gracefully if the file does not exist or cannot be read.

🛠️ Features

Reads input from a text file.

Writes a modified version of the file (lines are numbered and converted to uppercase).

Handles missing or unreadable files with clear error messages.

Demonstrates robust file handling and exception management.

📂 File Structure
week4_assignment.py     # Main Python script
sample.txt              # Example input file
modified_sample.txt     # Output file (created by program)
README.md               # Documentation

▶️ Usage

Clone or download this repository.

Ensure you have Python 3 installed.

Place a text file (e.g., sample.txt) in the same directory.

Run the script:

python week4_assignment.py


Enter the filename when prompted:

Enter the filename: sample.txt


The program will create a new file with a prefix modified_, e.g.:

modified_sample.txt

📝 Example
Input (sample.txt):
Hello world
This is my Python assignment
File handling is fun!

Output (modified_sample.txt):
1: HELLO WORLD
2: THIS IS MY PYTHON ASSIGNMENT
3: FILE HANDLING IS FUN!

🎯 Learning Outcomes

By completing this assignment, I practiced:

Opening, reading, and writing files in Python.

Using try/except for error handling.

Creating robust scripts that handle unexpected issues.

✨ This assignment is part of my PLP Python Week 4 challenge.
