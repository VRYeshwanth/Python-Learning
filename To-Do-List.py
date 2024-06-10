import json

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = {}
    return tasks

def save_task(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks, task_name):
    tasks[len(tasks)+1] = {"task_name": task_name, "completed": False}
    print("-------------------------------------------------")
    print("Task Added")
    print("-------------------------------------------------")

def display_tasks(tasks):
    if not tasks:
        print("-------------------------------------------------")
        print("No tasks to show")
        print("-------------------------------------------------")
    else:
        print("-------------------------------------------------")
        for task_number, task in tasks.items():
            print(f"{task_number}) {task["task_name"]} = {task["completed"]}")
        print("-------------------------------------------------")

def delete_task(tasks, task_number):
    if task_number in tasks:
        del tasks[task_number]
        print("-------------------------------------------------")
        print("Task Deleted")
        print("-------------------------------------------------")
    else:
        print("-------------------------------------------------")
        print("Task not found")
        print("-------------------------------------------------")

def complete_task(tasks, task_number):
    task = tasks.get(task_number)
    if task:
        if task["completed"] == False:
            task["completed"] = True
            print("-------------------------------------------------")
            print("Task Completed")
            print("-------------------------------------------------")
        else:
            task["completed"] = False
            print("-------------------------------------------------")
            print("Task Uncompleted")
            print("-------------------------------------------------")
    else:
        print("-------------------------------------------------")
        print("Task not found")
        print("-------------------------------------------------")

def edit_task(tasks, task_number, edit):
    task = tasks.get(task_number)
    if task:
        task["task_name"] = edit
        print("-------------------------------------------------")
        print("Task Edited")
        print("-------------------------------------------------")
    else:
        print("-------------------------------------------------")
        print("Task not found")
        print("-------------------------------------------------")

if __name__ == "__main__":
    print("Welcome to the To-Do List")
    while True:
        print("1) Add a new task")
        print("2) View all tasks")
        print("3) Delete a task")
        print("4) Complete/Uncomplete a task")
        print("5) Edit a task")
        print("6) Exit")
        try:
            ch = int(input())
            tasks = load_tasks()
            if ch == 1:
                task_name = input("Enter the name of your task : ")
                add_task(tasks, task_name)
                save_task(tasks)
            elif ch == 2:
                display_tasks(tasks)
            elif ch == 3:
                task_number = input("Enter the task number to delete it : ")
                delete_task(tasks, task_number)
                save_task(tasks)
            elif ch == 4:
                task_number = input("Enter the task number to complete/Uncomplete it : ")
                complete_task(tasks, task_number)
                save_task(tasks)
            elif ch == 5:
                task_number = input("Enter the task number to edit it : ")
                edit = input("Enter the text (to be edited) : ")
                edit_task(tasks, task_number, edit)
                save_task(tasks)
            elif ch == 6:
                exit(0)
        except ValueError:
            print("ERROR : Please enter a number")