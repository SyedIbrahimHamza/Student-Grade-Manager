# Student Grade Manager

A simple terminal-based **Student Grade Manager** built with Python. The program uses a menu-driven interface to add students, view student records, and search for students by roll number or name.

## What It Does

The program currently allows you to:

* Display a menu with student management options
* Add a new student
* Store the student's roll number and name
* Take marks for 5 subjects
* Store student records using Python dictionaries
* Store multiple students in a Python list
* View all stored student records
* Search for a student by roll number
* Search for a student by name
* Display a message when a student is not found
* Validate the menu choice before continuing

## Current Features

| Option | Feature                                   | Status         |
| ------ | ----------------------------------------- | -------------- |
| 1      | Add Student                               | ✅ Complete     |
| 2      | View All Students                         | ✅ Complete     |
| 3      | Search by Roll Number                     | ✅ Complete     |
| 4      | Search by Name                            | ✅ Complete     |
| 5      | Class Report (Topper, Average, Fail List) | 🔄 Coming Soon |
| 6      | Delete Student                            | 🔄 Coming Soon |
| 7      | Exit                                      | 🔄 Coming Soon |

## How to Run

Make sure Python is installed on your computer.

Run the program from the terminal:

```bash
python student_grade_manager.py
```

The program will display a menu and ask you to select an option from **1 to 7**.

## Menu

```text
=== STUDENT GRADE MANAGER ===
1. Add Student
2. View All Students
3. Search by Roll Number
4. Search by Name
5. Class Report (Topper, Average, Fail List)
6. Delete Student
7. Exit
```

The menu choice is validated using a `while` loop. If an invalid option is entered, the program asks the user to enter a number between 1 and 7.

## Add a Student

Select **1** to add a new student.

The program asks for:

* Roll number
* Student name
* Marks for 5 subjects

Example:

```text
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

Each student is stored as a dictionary:

```python
{
    'roll_number': '101',
    'name': 'Ali',
    'marks': [85.0, 78.0, 90.0, 88.0, 82.0]
}
```

Multiple student dictionaries are stored inside the `student` list.

## View All Students

Select **2** to display all students currently stored in the program.

Example:

```text
Enter your choice (1-7): 2

=== All Students ===
Roll Number: 101, Name: Ali, Marks: [85.0, 78.0, 90.0, 88.0, 82.0]
Roll Number: 102, Name: Ahmed, Marks: [75.0, 81.0, 79.0, 88.0, 90.0]
```

If no students have been added yet, the program displays:

```text
No students found.
```

## Search by Roll Number

Select **3** to search for a student using their roll number.

Example:

```text
Enter your choice (1-7): 3
Enter Roll Number to search: 101

Roll Number: 101, Name: Ali, Marks: [85.0, 78.0, 90.0, 88.0, 82.0]
```

The program loops through the student list and compares the entered roll number with each student's stored roll number.

If no matching student is found:

```text
Student not found.
```

The search uses a Boolean variable called `found` to keep track of whether a matching student exists. The `break` statement stops the search once a matching roll number is found.

## Search by Name

Select **4** to search for a student by name.

Example:

```text
Enter your choice (1-7): 4
Enter Name to search: ali

Roll Number: 101, Name: Ali, Marks: [85.0, 78.0, 90.0, 88.0, 82.0]
```

The name search is **case-insensitive** because the program converts both the stored name and entered name to lowercase:

```python
if s['name'].lower() == name.lower():
```

Therefore, searches such as:

```text
Ali
ali
ALI
aLi
```

can match the same student name.

If no matching student is found:

```text
Student not found.
```

## Data Structure

The program uses a **list of dictionaries** to store student records.

The main list is:

```python
student = []
```

Each student is stored as a dictionary containing three pieces of information:

```python
{
    'roll_number': roll_number,
    'name': name,
    'marks': marks
}
```

For example:

```python
student = [
    {
        'roll_number': '101',
        'name': 'Ali',
        'marks': [85.0, 78.0, 90.0, 88.0, 82.0]
    },
    {
        'roll_number': '102',
        'name': 'Ahmed',
        'marks': [75.0, 81.0, 79.0, 88.0, 90.0]
    }
]
```

## What I Learned

While building this project, I practiced:

* Using Python lists to store multiple student records
* Using dictionaries to organize student information
* Taking user input with `input()`
* Using `for` loops to collect marks for five subjects
* Using `float()` to convert marks into numbers
* Using `while` loops for menu control
* Validating user input
* Using `for` loops to search through student records
* Comparing roll numbers using conditional statements
* Performing case-insensitive string comparisons
* Using a Boolean variable such as `found` to track search results
* Using `break` to stop a search after finding a matching roll number
* Checking whether a list is empty before displaying records
* Appending dictionaries to a list

## Project Status

This project is currently **in progress**.

### Implemented

* ✅ Add students
* ✅ Store roll number, name, and marks
* ✅ View all students
* ✅ Search by roll number
* ✅ Search by name
* ✅ Case-insensitive name search
* ✅ Menu choice validation
* ✅ Empty student list handling

### Not Yet Implemented

The following options are currently displayed in the menu but their functionality has not yet been implemented:

* 🔄 Class Report
* 🔄 Topper calculation
* 🔄 Class average
* 🔄 Fail list
* 🔄 Delete Student
* 🔄 Exit functionality

## Future Improvements

Planned improvements include:

* Search students by partial name
* Calculate total marks
* Calculate student averages
* Identify the class topper
* Generate the class average
* Generate a list of failing students
* Delete student records
* Validate marks before storing them
* Prevent duplicate roll numbers
* Add a proper exit option
* Improve error handling for invalid mark input
* Improve the overall terminal interface

## Technologies Used

* **Python**
* Lists
* Dictionaries
* `while` loops
* `for` loops
* Conditional statements
* User input with `input()`
* Type conversion using `float()`

## Author

Built as a Python practice project to learn the fundamentals of lists, dictionaries, loops, conditions, user input, and basic student record management.
