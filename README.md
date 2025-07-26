# Daily Task Reminder Script

This repository contains a Python script designed to read tasks from a text file (`tasks.txt`) and filter and display only the tasks scheduled for today.

---

## Project Overview

- The script imports Python’s built-in `datetime` module, which is essential for handling dates.
- First, a function is defined to read all tasks from `tasks.txt`. It formats the task titles and dates properly to ensure clarity and consistency.
- After verifying the task reading function works correctly, another function is defined to filter tasks scheduled for today. It uses the `isoformat()` method to handle dates in the correct format (`YYYY-MM-DD`).
- The script loops through the filtered tasks:
  - If there are no tasks for today, it prints a message indicating so.
  - If tasks are found, it prints each task clearly.
- A simulated print statement is included to indicate where a reminder email would be sent for each task.
- The entire process is executed inside a main block following best Python practices.
- The output is formatted within a neat box-like structure to enhance readability and visual clarity.

---

## How to Run

1. Make sure both `daily_task_reminder.py` and `tasks.txt` are saved in the same folder.
2. Run the script using Python 3:
   python daily_task_reminder.py
3. Or, you can simply click on the run button if you have the Python extension installed on your VS Code.
