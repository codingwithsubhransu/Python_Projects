#add task
def addTask():
    task = input("Enter the task: ")
    status = "not done"
    with open("todolist.txt", "a") as f:
        f.write(f"{task}:{status}\n")
    print("Task added successfully")

def editTask(position):
    with open("todolist.txt", "r") as f:
        lines = f.readlines()
        if 1 > position or position > len(lines):   
                print("Invalid position or task")
                return
        print("1. Edit the task")
        print("2. Change the status")
        ch = int(input("Enter the choice: "))
        #split it to get the task line.
        task = lines[position-1].strip().split(":")
        if ch == 1:
            task[0] = input("Type the full task you want to change: ")
            lines[position-1] = ":".join(task)+"\n"
        elif ch == 2:
            task[1] = "Done"
            lines[position-1] = ":".join(task)+"\n"
        else:
            print("Invalid choice")
    #added the changed line
    with open("todolist.txt", "w") as f:
        f.writelines(lines)
        
    

def deleteTask(position):
    
    try:
        with open("todolist.txt", "r") as f:
            tasks = f.readlines()
            if position < 1 or position > len(tasks):
                print("Invalid position")
                return
            tasks.pop(position-1)

        with open("todolist.txt", "w") as f:
            f.writelines(tasks)
    except(ValueError, FileNotFoundError):
        print("File not found")


#display tasks

def displayTasks():
    with open("todolist.txt", "r") as f:
        tasks = f.readlines()
        if not tasks:
            print("File is empty ,add task")
            return
        for index,task in enumerate(tasks, 1):
            task_details = task.strip().split(":")
            print(f"{index}. {task_details[0]} - {task_details[1]}")



while True:
    print("-------------------------------------------------------------------------------------------------")
    print("1. Add Task")
    print("2. Change status or edit content")
    print("3. Delete Tasks")
    print("4. Display Tasks")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1: addTask()
    elif choice == 2:
        displayTasks()
        pos = int(input("Enter the position of the task you want to change or edit: "))
        editTask(pos)
    elif choice == 3: 
        displayTasks()
        pos = int(input("Enter the position to delete the task: "))
        deleteTask(pos)
    elif choice == 4:
        displayTasks()
    elif choice == 5:
        break
