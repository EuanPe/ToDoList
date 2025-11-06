def view_task(taskList):
    
    if len(taskList) == 0:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for task in taskList:
            print(f"{task['title']}, {task['dueDate']}-{task['complete']}\n")


            