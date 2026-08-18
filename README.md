# Student Grade Manager

A terminal-based student grade management system built with Python. The program uses a simple menu-driven interface to add students, view student records, and search for a student using their roll number.

## What it does

* Displays a menu with different student management options
* Allows you to add a new student
* Stores the student's roll number and name
* Takes marks for 5 subjects
* Stores student records using Python dictionaries
* Stores multiple students in a list
* Displays all student records
* Searches for a student by roll number
* Shows a message when a searched student is not found
* Validates the menu choice before continuing

## Current Features

| Option | Feature               | Status         |
| ------ | --------------------- | -------------- |
| 1      | Add Student           | ✅ Complete     |
| 2      | View All Students     | ✅ Complete     |
| 3      | Search by Roll Number | ✅ Complete     |
| 4      | Search by Name        | 🔄 Coming Soon |
| 5      | Class Report          | 🔄 Coming Soon |
| 6      | Delete Student        | 🔄 Coming Soon |
| 7      | Exit                  | 🔄 Coming Soon |

## How to run it

```bash
python student_grade_manager.py
```

Run the program in the terminal and choose an option from the menu.

### Add a Student

Select **1** and enter the student's roll number, name, and marks for five subjects.

### View All Students

Select **2** to display all students currently stored in the program.

### Search by Roll Number

Select **3** and enter a roll number. The program searches through the student list and displays the matching student's information.

If no student has that roll number, the program displays:

```text
Student not found.
```

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

Searching for the student:

```text
Enter your choice (1-7): 3
Enter Roll Number to search: 101

Roll Number: 101, Name: Ali, Marks: [85.0, 78.0, 90.0, 88.0, 82.0]
```

## What I learned building this

* Using a Python `list` to store multiple student records
* Using dictionaries to organize student information
* Taking user input with `input()`
* Using a `for` loop to collect marks for five subjects
* Using `float()` to convert marks into numbers
* Using `while` loops for menu control and input validation
* Using `for` loops to search through student records
* Using conditional statements to compare roll numbers
* Using a Boolean variable such as `found` to track search results
* Using `break` to stop searching once the student is found
* Checking whether a list is empty before displaying records

## Project Status

This project is currently **in progress**.

The following functionality has been implemented:

* Adding students
* Viewing all students
* Searching students by roll number

The remaining menu options will be implemented in future updates.

## Future Improvements

* Search students by name
* Calculate student totals and averages
* Identify the class topper
* Generate a class average
* Generate a list of failing students
* Delete student records
* Add validation for marks
* Prevent duplicate roll numbers
* Add a proper exit option
* Improve the overall terminal interface
