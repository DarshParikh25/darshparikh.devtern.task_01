TASKS_FILE = "tasks.txt"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks():
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

tasks = load_tasks()

def add_todo():
    task = input("Enter the name of the task :")
    task_name = task + " - m"
    tasks.append(task_name)
    save_tasks()
    print("Task has been added successfully!")

def update_task():
    if len(tasks) == 0:
        print("There is no task in the to-do list to update!")
    else:
        i = 1
        for items in tasks:
            print(f"{i} : {items}")
            i += 1
    up_choice = int(input("Enter the number of the task to be updated :"))
    if up_choice <= 0:
        print("Invalid task number!")
    else:
        up_task = input("Enter the name of the updated task :")
        tasks[up_choice - 1] = up_task
        # tasks.insert(up_choice, up_task)
        save_tasks()
        print("The task has been updated successfully!")

def mark_comp_task():
    if len(tasks) == 0:
        print("There is no task in the to-do list to update!")
    else:
        i = 1
        for items in tasks:
            print(f"{i} : {items}")
            i += 1
    mac_choice = int(input("Enter the number of the task to be marked as completed :"))
    if mac_choice <= 0:
        print("Invalid task number!")
    else:
        comp = tasks[mac_choice - 1] + " - COMPLETED"
        tasks.insert(mac_choice - 1, comp)
        save_tasks()
        print("The task has been successfully marked as complete!")

def del_task():
    if len(tasks) == 0:
        print("There is no task to delete in the to-do list!")
    else:
        i = 1
        for items in tasks:
            print(f"{i} : {items}")
            i += 1
        del_choice = int(input("Enter the task number to be deleted :"))
        if del_choice <= 0:
            print("Invalid task number!")
        else:
            del tasks[del_choice - 1]
            save_tasks()
            print("Task deleted successfully!")

def set_due_date():
    if len(tasks) == 0:
        print("There is no task to set due date in the to-do list!")
    else:
        i = 1
        for items in tasks:
            print(f"{i} : {items}")
            i += 1
    dd_choice = int(input("Enter the task number to set priority :"))
    if dd_choice <= 0:
        print("Invalid task number!")
    else:
        due_date = input("Enter the due date of the task :")
        tasks.insert(dd_choice - 1, f"\tDue Date : {due_date}")


def set_priority():
    PRIORITY = ["c", "h", "m", "l", "o"]
    print("c : crucial")
    print("h : high")
    print("m : medium")
    print("l : low")
    print("o : optional")
    if len(tasks) == 0:
        print("There is no task to set priority in the to-do list!")
    else:
        i = 1
        for items in tasks:
            print(f"{i} : {items}")
            i += 1
    prior_choice = int(input("Enter the task number to set priority :"))
    if prior_choice <= 0:
        print("Invalid task number!")
    else:
        priority = input("Enter the priority of the task from above :")
        tasks.insert(prior_choice - 1, f"\tPriority : {priority}")
        # if priority == "c":
        #     list.insert(0, list[prior_choice - 1])
        #     del list[prior_choice]
        #     print("Priority of the task is successfully set!")
        # elif priority == "h":

def view_tasks():
    if len(tasks) == 0:
        print("There is no task in the to-do list!")
    else:
        i = 1
        for items in tasks:
            print(f"{i} : {items}")
            i += 1

def main():
    while True:
        print("\n-----To-Do List-----")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Mark as Complete Task")
        print("4. Delete Task")
        print("5. Set Task Due Date")
        print("6. Set Task Priority")
        print("7. View Tasks")
        print("8. Exit")
        choice = int(input("Enter your choice :"))
        if choice == 1:
            add_todo()
        elif choice == 2:
            update_task()
        elif choice == 3:
            mark_comp_task()
        elif choice == 4:
            del_task()
        elif choice == 5:
            set_due_date()
        elif choice == 6:
            set_priority()
        elif choice == 7:
            view_tasks()
        elif choice == 8:
            break
        else:
            print("Invalid choice! Please try again!")

if __name__ == "__main__":
    main()

list = ["a", "b", "c"]
ind = list.index("b")
item = list[ind]
list.insert(0, item)
del list[ind + 1]
print(list)