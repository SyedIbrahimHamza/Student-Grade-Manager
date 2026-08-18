# Student Grade Manager

A terminal-based student grade management system built with Python. The program allows users to add student records and view all students through a simple menu-driven interface.

## What it does

* Displays a menu with different student management options
* Allows you to add a new student
* Stores the student's roll number and name
* Takes marks for 5 subjects
* Stores student information using Python dictionaries
* Stores multiple students in a list
* Displays all saved student records
* Validates the main menu choice before continuing

## Current Features

| Option | Feature               | Status         |
| ------ | --------------------- | -------------- |
| 1      | Add Student           | ✅ Complete     |
| 2      | View All Students     | ✅ Complete     |
| 3      | Search by Roll Number | 🔄 Coming Soon |
| 4      | Search by Name        | 🔄 Coming Soon |
| 5      | Class Report          | 🔄 Coming Soon |
| 6      | Delete Student        | 🔄 Coming Soon |
| 7      | Exit                  | 🔄 Coming Soon |

## How to run it

```bash
python student_grade_manager.py
```

Run the program in the terminal and choose an option from the menu.

To add a student, select **1**, then enter the student's roll number, name, and marks for five subjects.

To view all students, select **2**.

## Example

```text
=== STUDENT GRADE MANAGER ===
1. Add Student
2. View All Students
3. Search by Roll Number
4. Search by Name
5. Class Report (Topper, Average, Fail List)
6. Delete Student
7. Exit

Enter your choice (1-7): 1

Enter Roll Number: 101
Enter Name: Ali
Enter marks for subject 1: 85
Enter marks for subject 2: 78
Enter marks for subject 3: 90
Enter marks for subject 4: 88
Enter marks for subject 5: 82

Student added successfully.
```

## What I learned building this

* Using a Python `list` to store multiple student records
* Using dictionaries to organize student information
* Taking user input with `input()`
* Using a `for` loop to collect marks for five subjects
* Using `float()` to convert marks from text to numbers
* Using `while` loops for menu control and input validation
* Using conditional statements to handle different menu choices
* Accessing dictionary values using keys
* Checking whether a list is empty before displaying records

## Project Status

This project is currently **in progress**.

The basic student record functionality has been implemented. Search, class reports, deletion, and the exit functionality will be added in future updates.

## Future Improvements

* Search students by roll number
* Search students by name
* Calculate student totals and averages
* Identify the class topper
* Generate a list of failing students
* Delete student records
* Add validation for marks
* Prevent duplicate roll numbers
* Add a proper exit option
