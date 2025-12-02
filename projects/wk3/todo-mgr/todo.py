#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: todo.py
Author: Joe
Date: 2025-11-30
Version: 0.1.0
Description: application to manage a to do list in a .txt file
"""

# import ipdb; ipdb.set_trace()

# todo-mgr/
TASKS = "tasks.txt"
COMPLETED = "completed.txt"

# Functions
def get_user_input():
    """Accept user input and parse to confirm format"""
    while True:
        user_input = input(" > ").strip().lower()
        if user_input == 'q':
            break
        return user_input

def pending_or_completed():
    user_input = get_user_input()
    if user_input == 'p':
        return user_input
    elif user_input == 'c':
        return user_input


def add_task(user_content):
    """# append to tasks list"""
    user_input = input(" + ")
    user_input = user_input.strip()
    user_content.append(user_input)
    print(f"✅ Added task: {user_input}")
    return user_content

def remove_task(tasks, completed):
    """Remove from task list"""
    user_input = None
    list_edited = None
    while user_input != 'q':
        print("Enter 'p' to remove pending tasks or 'c' to remove completed tasks or 'q' to quit")
        user_input = input("(p/c): ").strip().lower()
        
        if user_input == 'q':
            break
        elif user_input == 'p':
            user_content = tasks
            list_edited = 'tasks'
        elif user_input == 'c':
            user_content = completed
            list_edited = 'completed'
        else:
            continue 

        print("Which task would you like to remove?")
        for index, task in enumerate(user_content, start=1):
            print(f"Task {index}: {task}")
        user_input = get_user_input()
        # Break before doing removals if user entered 'q'
        user_input = int(user_input)
        remove_index = user_input - 1

        remove_task = user_content.pop(remove_index)
        if list_edited == 'tasks':
            print(f"Removed from {list_edited}, Task {user_input}: 🔲 {remove_task}") 
        elif list_edited == 'completed':
            print(f"Removed from {list_edited}, Done {user_input}: ✅ {remove_task}")
        if user_input == 'p':
            tasks = user_content
            continue
        elif user_input == 'c':
            completed = user_content
            continue
        elif user_input == 'q':
            return tasks, completed
        else:
            break

    return tasks, completed

def remove_all_tasks(tasks, completed):
    tasks, completed = [], []
    return tasks, completed

def mark_complete(tasks, completed):
    """Move tasks to completed.txt"""
    user_input = None
    completed_index = None
    # while user_input != 'q':
    print(f"Task List\n")
    print(f"item\ttask")
    print("Which task would you like to mark complete?") 
    for index, task in enumerate(tasks, start=1):
        print(f"{index}\t🔲 {task}")
    while True:
        """Complete loop for tasks"""
        user_input = input(" : ").lower().strip()
        
        if user_input == 'c':
            break
        elif user_input == 'q':
            break
        
        # elif user_input == 's':
        #     print(f"Writing completed tasks...")
        #     return tasks, completed
        
        try:
            completed_index = int(user_input) - 1
        except ValueError as e:
            continue
        try:
            completed_task = tasks.pop(completed_index)
            completed.append(completed_task)
            print(f"✅ Marked task {completed_task} complete")
        except IndexError as e:
            continue
        print("Enter 'c' to finish or another task number to mark as complete")
    return tasks, completed
    # maybe add "[DONE]" prefix or move to separate list

def display_content(user_content, is_completed = None):
    """Print enumerated tasks with index numbers"""
    if is_completed == 1:
        print(f"Completed List\n")
        print(f"item\ttask")
        for index, task in enumerate(user_content, start=1):
            print(f"{index}\t✅ {task}")
    else:
        print(f"Task List\n")
        print(f"item\ttask")
        for index, task in enumerate(user_content, start=1):
            print(f"{index}\t🔲 {task}")

def save_to_file(user_content, filename):
    """Write list to file, one item per line"""
    with open(filename, 'w') as f:
        for item in user_content:
            f.write(item + '\n')
    print(f"✅ Saved! '{filename}' updated.")

def print_menu():
    """Main loop with menu"""
    print("What would you like to do? (Press 'q' to quit)")
    print("   n. Create new task")
    print("   c. Mark pending task as complete")
    print("   r. Remove a task")
    print("   p. Show all pending tasks")
    print("   d. Show all done / completed tasks")
    print("   s. Save and quit")
    print("   x. Delete all tasks")
    print("   h. Print help menu")

def main():
    with open(TASKS, 'r') as f:
        tasks = f.read().splitlines()
    with open(COMPLETED, 'r') as f:
        completed = f.read().splitlines()

    user_input = None
    print_menu()
    while user_input != 'q':
        """Main loop with menu"""
        user_input = input(" > ")
        try:
            user_input = str(user_input.strip().lower())
        except ValueError as e:
            continue
        match user_input:
            case 'n':
                tasks = add_task(tasks)
                # save_to_file(tasks, TASKS)
                # print(f"✅ New task added and tasks.txt file updated.")
                continue
            case 'r':
                tasks, completed = remove_task(tasks, completed)
                # save_to_file(tasks, TASKS)
                continue
            case 'x':
                print(f"Warning!")
                print(f"You are about to delete all pending and completed tasks!")
                print(f"Are you sure you'd like to proceed? (y/n)")
                user_input = get_user_input()
                if user_input == 'y':
                    tasks, completed = remove_all_tasks(tasks, completed)
                elif user_input == 'n':
                    continue
                else:
                    continue

            case 'c':
                tasks, completed = mark_complete(tasks, completed)
                # save_to_file(tasks, TASKS)
                # save_to_file(completed, COMPLETED)
                continue
            case 'p':
                display_content(tasks)
                continue
            case 'd':
                display_content(completed, is_completed=1)
                continue
            case 's':
                save_to_file(tasks, TASKS)
                save_to_file(completed, COMPLETED)
                continue
            case 'h':
                print_menu()
                continue
            case 'q':
                print(f"Warning!")
                print(f"You are about to quit without saving.")
                print(f"Would you like to save first? (y/n)")
                while True:
                    quit_test = get_user_input()
                    if quit_test == 'y':
                        save_to_file(tasks, TASKS)
                        save_to_file(completed, COMPLETED)
                        user_input = 'q'
                        break
                    elif quit_test == 'n':
                        user_input = 'q'
                        break
                continue
            # case # Catch all for other case?

if __name__ == "__main__":
    main()
