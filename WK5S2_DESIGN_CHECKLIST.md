# To-Do List Application - Design Document

**Team Name**: Clutchmatez

**Team Members**: Ben, Euan, Aiman, Azfa
 

**Date**: 30 October 2025

---

## 1. Requirements Analysis

### 1.1 Research Notes
After exploring existing to-do list applications (Microsoft To-Do, Trello, GitHub Projects, etc.), we observed the following common features:

**What can these applications do?**
-Track/Remind users task
-Tick off the tasks option
-Search the tasks

**What data do they store?**
-Date of creation/To do
-Time of creation/To do
-Name/Title of the task

**How do they display data?**
-Tabs
-List
-Filter

---

### 1.2 Essential Features
List the features your to-do list MUST have to be functional:

1.Able to save the task
2.Able to view the task
3.Able to remind the users
4.Able to sort the task
5.Able to describe the task

**Why are these essential?**

To give users easy access on the tasks and keep the tasks organised.
---

### 1.3 Desirable Features
List nice-to-have features that would enhance the application but aren't strictly necessary:

1.Notification
2.Collaboration
3.Task cal
4.Assign people tasks

---

## 2. Data Structure Design

### 2.1 Task Data
What information does each individual task need to store?

| Data Field | Data Type | Purpose         | Example |
|------------|-----------|---------        |---------|
|Task ID     |String     |To identify taks |T65934 |
|Task title  |String     |To describe tasks|Reading time|
|Task Due date|DateTime  To display the due date| 01/10/2025
|Complete    |Boolean   | check if complete| true     |
---

### 2.2 Task List Structure
How will you store the collection of tasks?

**Chosen Structure** (e.g., list of dictionaries, list of lists, list of tuples):
-list of dictionaries

**Why did you choose this structure?**
Easier to store multiple data types

**Example of your data structure with 2-3 sample tasks**:
```python
# Write your example here
T658473, homework, 01/12/2025, false
T937449, cleaning, 03/09/2025, true

list[2]{Description}			
```

**How will you access specific fields?** (e.g., for list of dicts: `task["description"]`)

# Returns id for searched task
for allTasks: 
	if allTasks[i,1] == searchvalue:
	return allTasks[i,1]
	

---

## 3. Input/Output Design

### 3.1 Keyboard Input
What inputs will need to be provided?

| Input Type | When Required | Validation Needed |
|------------|---------------|-------------------|
|integer     |when asked to choose a function |type check, range check, presence check|
|string      |when asked for a search value |length check, presence check |

---

### 3.2 Screen Output
How will you display information?

**Menu Design**:
```
--TASKS--

name/due date/status
Cleaning - 11/04/2024 - complete

1. Add task
2. Search task
3. Delete task
4. filter task
5. view task


```

**Task Display Format**:
```
[Show how you'll display a list of tasks]




```

---

### 3.3 File I/O
How will you handle file operations?

**File format** (CSV, JSON, plain text, etc.):

CSV file

**Why this format?**

separate fields by commas so they are easily accessible

**Example of file structure**:
```
[Show what your saved file will look like]

id/title/dueDate/complete
T4638230,Homework,05/11/2025,true

```

**When will you load data?**

load data on start up to display all tasks 


**When will you save data?**

save data when deleting, adding or editing a task

---

## 4. Program Flow



### 4.1 Main Loop Structure
Describe or draw a flowchart of how your program will run:


```
[Pseudocode or description of main loop]
1. display all tasks on start up
2. give options to manipulate tasks
```

---

### 4.2 Error Handling
What could go wrong, and how will you handle it?

| Potential Error | How to Handle |
|----------------|---------------|
| File doesn't exist | output "file not found" , sys.exit()|
| Invalid user input | output "invalid input, please enter a number 1-...", ask again|
| Empty task list | if task list is empty, only option is to add a new task|
| | |

---

## 5. Function Specifications

For each function your team will implement, specify:
- Function name
- Purpose
- Parameters (with types)
- Return value (with type)
- Brief description of what it does

### Example:
```python
def add_task(task_list, description, priority):
    '''
    Add a new task to the task list.

    Parameters:
        task_list (list): The list of all tasks
        description (str): The task description
        priority (str): Priority level ('high', 'medium', 'low')

    Returns:
        list: Updated task list with the new task added
    '''
    pass
```

### Your Functions:

**Function 1:**
```python




```

**Function 2:**
```python




```

**Function 3:**
```python




```

**Function 4:**
```python




```

**Function 5:**
```python




```

**Function 6:**
```python




```

*(Add/ remove functions as needed)*

---

## 6. Peer Feedback Record

### Feedback Received (from other team):
**Date**: _________  **Reviewing Team**: _________________

**Strengths of our design**:
-
-

**Suggestions for improvement**:
-
-

**Changes we made after feedback**:
-
-

---

### Feedback Given (to other team):
**Date**: _________  **Team Reviewed**: _________________

**What we liked**:
-
-

**Constructive suggestions**:
-
-

---

## 7. Design Decisions Log

As you work through the design, record important decisions and why you made them:

| Decision | Options Considered | Final Choice | Reasoning |
|----------|-------------------|--------------|-----------|
| | | | |
| | | | |
| | | | |

---

## 8. Next Steps

Before starting implementation, make sure:

- [ ] All team members understand the data structure
- [ ] All function signatures are agreed upon
- [ ] Everyone knows which functions they will implement
- [ ] Git repository is set up and all members have access
- [ ] Branch naming strategy is agreed
- [ ] Testing approach is discussed (Next week's class will cover this)

**Ready to code?** Make sure all boxes are ticked!