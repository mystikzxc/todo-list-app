# Location for tasks file
FILE_LOCATION = "todo-list-app/tasks.txt"

# Tasks list
tasks = []

# Function to load tasks
def load_tasks():
    # Open tasks file and add tasks to list
    tasks_file = open(FILE_LOCATION, "r")

    for task in tasks_file:
        tasks.append(task.strip())

    tasks_file.close()

# Function to add a task
def add_task(task):
    tasks.append(task)
    print(f"Succesfully created task: {task}")

# Function to remove a task
def remove_task(task):
    # Validates if task is in tasks
    try:
        tasks.remove(task)
        print(f"Successfully deleted task: {task}")
    except ValueError:
        print(f"Task: {task} cannot be found")

# Function to show all tasks
def show_tasks():
    print("TASKS:")

    for task in tasks:
        print(task)

# Function save tasks to a file
def save_tasks():
    print("Saving tasks and closing app...")

    # Open tasks file, write tasks and close
    tasks_file = open(FILE_LOCATION, "w")
    for task in tasks:
        tasks_file.write(str(task) + "\n")
    tasks_file.close()


# Main function to load tasks and loop the menu
def main():
    # Display menu in a loop until Exit
    load_tasks()

    while True:
        print("----------")
        print("MENU:")
        print("(1) Add Task\n(2) Remove Task\n(3) Show Tasks\n(4) Exit")
        print("----------")

        selection = input("Make a selection: ")

        if selection == "1": # Add Task
            task = input("Create Task: ")
            add_task(task)
        elif selection == "2": # Remove Task
            task = input("Remove Task: ")
            remove_task(task)
        elif selection == "3": # Show Tasks
            show_tasks()
        elif selection == "4": # Exit
            save_tasks()
            break
        else:
            print("Incorrect selection")

if __name__ == "__main__":
    main()