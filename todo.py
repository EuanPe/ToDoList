import sys

def read_data(filename):
    taskList = []
    with open(filename, "r") as infile:
        next(infile) # Skip header line
        for line in infile:
            parts = line.strip().split(",")
            if len(parts) == 4:
                task = {
                    "id": int(parts[0]),
                    "title": parts[1],
                    "dueDate": parts[2],
                    "complete": parts[3]
                }
                taskList.append(task)
    return taskList

def save_data(filename, taskList):
    with open(filename, "w") as outfile:
        outfile.write("id,title,dueDate,complete\n") # Header line
        for task in taskList:
            outfile.write(f"{task['id']},{task['title']},{task['dueDate']},{task['complete']}\n")


def add_task(taskList):
    invalid = True
    while invalid:
        title = input("please enter a task title")
        dueDate = input("please enter a task due date")
        if title and len(title) < 20: # validation for title
            if len(dueDate) == 10 and dueDate[2] == "/" and dueDate[5] == "/": # Validation for due date
                invalid = False
            else:
                print("please ensure due date is formatted dd/mm/yyyy")
        else:
            print("please ensure title is less than 20 character and greater than 0")


    if taskList:
        new_id = max(task["id"] for task in taskList) + 1
    else:
        new_id = 1

    complete = False
    newTask = {"id":new_id,  "title":title, "dueDate": dueDate, "complete": complete}
    taskList.append(newTask)
    save_data("All_Tasks.CSV",taskList)



def run_program():
    taskList = read_data("All_Tasks.CSV")
    home_choice = int(input("Please select an option: \n1) Add task \n2) Search task \n3) Delete task \n4) Filter tasks \n5) View tasks \n6) Exit\n"))
    match home_choice:
        case 1:
            add_task(taskList)
        case 2:
            search_task(taskList)
        case 3:
            delete_task(taskList)
        case 4:
            filter_task(taskList)
        case 5:
            view_tasks(taskList)
        case 6:
            sys.exit()
        case _:
            print("incorrect value entered, please enter a number 1-6")

run_program()