#To-Do-List is a type of Method which is used to manage useful
#project that helps users to manage and organize their tasks efficiently.

class ToDoList():
    def __init__(self):
        self.tasks=[]
        
    def display_tasks(self):
        print("To-Do-List")
        for i, task in enumerate(self.tasks,1):
            print(f"{i}. {task}")
            
    def add_task(self):
        self.task = input("Enter the  task: ")
        if self.task != "":
            self.tasks.append(self.task)
            print(f"Task {self.task} is added successfully to the List.")
            
    def delete_task(self):
        task_number = int(input("Enter the task number to delete: "))
        try:
            del self.tasks[task_number - 1]
            print(f"Task {task_number} is deleterd successfully.")
        except IndexError:
            print("Invalid task number.")
            
    def update_task(self):
        task_number = int(input("Enter the task number to be updated: "))
        try:
            task = input("Enter the new task: ")
            if task != "":
                self.tasks[task_number - 1] = task
                print(f"Task {task_number} updated successfully.")
        except IndexError:
            print("Invalid task number.")
                
ToDo_List = ToDoList()
while True:
    print("\nTo-Do-List Menu: ")
    print("1. Display Tasks")
    print("2. Add task")
    print("3. Delete Task")
    print("4. Update Task")
    print("5. Quite")

    choice = int(input("Enter the choice: "))

    if choice == 1:
        ToDo_List.display_tasks()
    elif choice == 2:
         ToDo_List.add_task()
    elif choice == 3:
         ToDo_List.delete_task()
    elif choice == 4:
         ToDo_List.update_task()
    elif choice == 5:
         print("Goodbye!")
         break
    else:
        print("Invalid choice. Please Enter correct number: ")
        
        
