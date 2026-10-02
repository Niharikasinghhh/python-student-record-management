# Student Record Management System

A beginner-friendly Student Record Management System built using Python. This command-line application allows users to add, view, search, and delete student records using file handling.

## Features

- Add new student records
- View all student records
- Search for a student using their ID
- Delete student records
- Prevent duplicate student IDs
- Interactive command-line menu
- Automatically creates the data file if it does not exist

## Technologies Used

- Python 3
- VS Code
- Git and GitHub

## Python Concepts Practiced

- File handling using open()
- File modes: read (r), append (a), and write (w)
- read(), readlines(), and write()
- with statement
- Functions
- Loops and conditional statements
- User input and string methods
- Basic CRUD operations

## Project Structure

```text
python-student-record-management/
├── Main.py
├── students.txt
└── README.md
```

## How to Run

1. Install Python 3.
2. Clone this repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/python-student-record-management.git
   ```

3. Open the project folder:

   ```bash
   cd python-student-record-management
   ```

4. Run the program:

   ```bash
   python Main.py
   ```

## Data Storage

Student records are stored in students.txt. Each record contains an ID, name, and marks, separated by commas.

Example:

```text
101,Niharika,90
102,Aarav,85
```

The program creates students.txt automatically if it is missing.

## Purpose

This project was created to practice Python fundamentals and understand how file handling can be used to build a simple record management application.

## Author

Niharika Singh
