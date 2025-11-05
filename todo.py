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
                    "complete": parts[3].lower()
                }
                taskList.append(task)
    return taskList

def save_data(filename, taskList):
    with open(filename, "w") as outfile:
        outfile.write("id,title,dueDate,complete\n") # Header line
        for task in taskList:
            outfile.write(f"{task['id']}, {task['title']}, {task['dueDate']}, {task['complete']}\n")


def add_task(title, dueDate):
    taskList = read_data("All_Tasks.CSV")
    if taskList:
        new_id = max(task["id"] for task in taskList) + 1
    else:
        new_id = 1

    complete = False
    newTask = {"id":new_id, "title":title, "dueDate": dueDate, "complete": complete}
    taskList.append(newTask)
    save_data("All_Tasks.CSV",taskList)

title = input("please enter a task title")
dueDate = input("please enter a task due date")

add_task(title,dueDate)

print(read_data("All_Tasks.CSV"))