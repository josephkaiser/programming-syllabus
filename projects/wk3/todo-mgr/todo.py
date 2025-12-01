#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: todo.py
Author: Joe
Date: 2025-11-30
Version: 0.1.0
Description: application to manage a to do list in a .txt file
"""

# import pdb; pdb.set_trace()

# todo-mgr/
TASKS = "tasks.txt"
COMPLETED = "completed.txt"

# Functions
def add_task(user_content):
    """# append to tasks list"""
    task = input(" + ")
    user_content.append(task)
    return user_content

def remove_task(user_content):
    """Remove from task list"""
    print("Which task would you like to remove?")
    remove_index = None
    while remove_index != 'q':
        """Remove loop for tasks"""
        for index, task in enumerate(user_content):
            print(f"Task {index}: {task}")
        remove_index = input(" > ")
        try:
            remove_index = int(remove_index.strip())
        except:
            break
        remove_task = user_content.pop(remove_index)
        print(f"Removed {remove_task}")
    return user_content

def mark_complete(tasks, completed):
    """Move tasks to completed.txt"""
    print("Which task would you like to mark complete (type e to end)?")
    completed_index = []
    while completed_index != 'q':
        """Complete loop for tasks"""
        if completed_index == 'e':
            return tasks, completed
        for index, task in enumerate(tasks):
            print(f"Task {index}: {task}")
        completed_index = input(" > ")
        try:
            completed_index = int(completed_index.strip())
        except:
            break
        completed_task = tasks.pop(completed_index)
        completed.append(completed_task)
    # print(f"Marked task {completed_task} complete")
    return tasks, completed
    # maybe add "[DONE]" prefix or move to separate list

def display_content(user_content):
    """Print enumerated tasks with index numbers"""
    for index, task in enumerate(user_content):
        print(f"Task {index}: {task}")

def save_to_file(user_content, filename):
    """Write list to file, one item per line"""
    with open(filename, 'w') as f:
        for item in user_content:
            f.write(item + '\n')


def main():
    with open(TASKS, 'r') as f:
        tasks = f.read().splitlines()
    with open(COMPLETED, 'r') as f:
        completed = f.read().splitlines()

    user_input = 0
    while user_input != 'q':
        """Main loop with menu"""
        print("What would you like to do? (Press 'q' to quit)")
        print("1. Add task")
        print("2. Remove task")
        print("3. Mark complete")
        print("4. Display pending tasks")
        print("5. Display completed tasks")
        print("6. Save and quit")
        user_input = input(" > ")
        user_input = int(user_input)
        match user_input:
            case 1:
                tasks = add_task(tasks)
                display_content(tasks)
                continue
            case 2:
                tasks = remove_task(tasks)
            case 3:
                tasks, completed = mark_complete(tasks, completed)
            case 4:
                display_content(tasks)
            case 5:
                display_content(completed)
            case 6:
                save_to_file(tasks, TASKS)
                save_to_file(completed, COMPLETED)
        
        user_input = input("Press 'q' to quit or hit enter to continue")

if __name__ == "__main__":
    main()
