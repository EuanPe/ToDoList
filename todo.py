def search_task(taskList):
    target = input("Enter the title of the task you are looking for: ")

    for i in range (len(taskList)):
        if target.strip().lower() in taskList[i]["title"]:
            if taskList[i]["complete"] == "True":
                complete = "Completed"
            else:
                complete = "Incomplete"

            print(f"{taskList[i]["title"]} - {taskList[i]["dueDate"]} - {complete}")
            update_task(taskList)

def update_task(taskList):
    choice = int(input("Would you like to update a task?\n1)yes\n2)no"))
    if choice == 1: 
        title = input("Please enter the title of the task you want to update")
        for i in taskList:
            if title == taskList[i]["title"]:
                taskList[i]["complete"] = "True"
                print("Task successfully updated")
            else:
                print("task does not exist")
    else: 
        run_program()

def delete_task (taskList):
    target = input("Enter the title of the task you want to delete: ")
    print("Results: ")
    for i in range (len(taskList)):
        if target.strip().lower() in taskList[i]["title"]:
            if taskList[i]["complete"]:
                complete = "Completed"
            else:
                complete = "Incomplete"
            print(f"{taskList[i]["id"]} {taskList[i]["title"]} - {taskList[i]["dueDate"]} - {complete}")
    ID = int(input("Please enter the ID of the task you want to delete: "))
    for i in range (len(taskList)-1):
        if ID == taskList[i]["id"]:
            taskList.remove(taskList[i])
            print("Task removed successfully")
    
    save_data("All_Tasks.CSV", taskList)
    
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


def view_tasks(taskList):
    
    if len(taskList) == 0:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for task in taskList:
            if task["complete"] == "True":
                complete = "Completed"
            else:
                complete = "Incomplete"

            spaces = 20 - len(task["title"])
            task["title"] = task["title"].ljust(spaces + len(task["title"]))
            print(f"{task["title"]}| {task["dueDate"]} | {complete} ")
            update_task(taskList)


def sort_tasks(taskList) : 
    print("\n Sort taks by :")
    print("1) Title : ")
    print("2) Duedate : ")
    print("3) Completion Status : ")

    choice = int(input("Enter your choice (1-3) : "))

    if choice == 1 : 
        sorted_list = (sorted(taskList, key = lambda x: x["title"].lower() ))
        print("\nTasks sorted by title are : ")
    elif choice == 2 : 
        sorted_list = (sorted(taskList, key = lambda x: x["dueDate"].lower() ))
        print("\nTasks sorted by duedate are : ")
    elif choice == 3 : 
        sorted_list = (sorted(taskList, key = lambda x: x["completed"].lower() ))
        print("\nTasks sorted by completion status are : ")
    else : 
        print("Invalid choice. ")
    
    for task in sorted_list : 
        if task["complete"] == "True":
            complete = "Completed"
        else:
            complete = "Incomplete"

        spaces = 20 - len(task["title"])
        task["title"] = task["title"].ljust(spaces + len(task["title"]))
        print(f"{task["title"]}| {task["dueDate"]} | {complete} ")

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
            sort_tasks(taskList)
        case 5:
            view_tasks(taskList)
        case 6:
            sys.exit()
        case _:
            print("incorrect value entered, please enter a number 1-6")

run_program()
