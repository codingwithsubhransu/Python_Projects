#Todo list to take input output edit in cmd.
'''Features of todo list:-
        -> add a new work.
        -> select done or not done.
        -> Delete
        -> Exit
'''

'''
    we can use linkedlist for this.
'''

TaskList = []
class Task:
    def __init__(self, data, done=False):
        self.data = data
        self.done = done
        self.next = None

class TodoList:
    def __init__(self):
        self.head = None

    def addTask(self, data):
        new_task = Task(data)
        if self.head is None:
            self.head = new_task
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_task

    def deleteTask(self, position):
        if self.head is None:
            print("No tasks to delete.")
            return
        if position == 1:
            self.head = self.head.next
            return
        
        temp = self.head
        index = 1
        while temp and index < position - 1:
            temp = temp.next
            index += 1

        if temp is None or temp.next is None:
            print("Invalid position")
            return
        
        temp.next = temp.next.next

    def markdone(self, position):
        if self.head is None:
            print("No tasks to mark.")
            return
        
        temp = self.head
        index = 1
        while temp and index < position:
            temp = temp.next
            index += 1
        
        if temp is None:
            print("Invalid position.")
            return
        
        temp.done = True
        print(f"Task at position {position} marked as done.")

    def editTask(self, position):
        if self.head is None:
            print("No tasks to edit.")
            return

        index = 1
        temp = self.head
        while temp and index < position:
            temp = temp.next
            index += 1
        
        if temp is None:
            print("Invalid position.")
            return
        
        new_task = input(f"Edit the task '{temp.data}': ")
        temp.data = new_task
        print(f"Task at position {position} has been updated.")

    def display(self):
        index = 1
        if self.head is None:
            print("No tasks available.")
            return
        
        temp = self.head
        while temp:
            status = "completed" if temp.done else "not done"
            print(f"{index}. {temp.data} is {status}")
            temp = temp.next
            index += 1


# Main interaction loop
todo = TodoList()
while True:
    print("\n1. Add task")
    print("2. Mark task as done")
    print("3. Delete task")
    print("4. Display tasks")
    print("5. Edit task")
    print("6. Exit")
    choice = int(input("Choose an option: "))
     
    if choice == 1:
        task = input("Add your task: ")
        todo.addTask(task)

    elif choice == 2:
        todo.display()
        pos = int(input("Enter the task's position you want to mark as done: "))
        todo.markdone(pos)

    elif choice == 3:
        todo.display()
        pos = int(input("Enter the task's position you want to delete: "))
        todo.deleteTask(pos)

    elif choice == 4:
        todo.display()
    
    elif choice == 5:
        todo.display()
        pos = int(input("Enter the task's position you want to edit: "))
        todo.editTask(pos)
    
    elif choice == 6:
        break

    else:
        print("Invalid choice. Please try again.")
