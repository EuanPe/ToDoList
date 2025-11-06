def search_task(taskList):
    target = input("Enter the title of the task you are looking for: ")

    for i in range (len(taskList)):
        if target.strip().lower() in taskList[i]["title"]:
            if taskList[i]["complete"]:
                complete = "Completed"
            else:
                complete = "Incomplete"

            print(f"{taskList[i]["title"]} - {taskList[i]["dueDate"]} - {complete}")



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
    ID = input("Please enter the ID of the task you want to delete: ")
    for i in range (len(taskList)):
        if ID == taskList[i]["id"]:
            taskList.remove(taskList[i])
            print("Task removed successfully")
    
    save_data("All_Tasks.CSV", taskList)
