# To Do List Manager

For Python syllabus week 3 project. 

### Specs:
- Command-line todo list manager application with persistent storage using a text file
- Functions: add tasks, mark complete, remove tasks, display all, save to/load from file

#### Main CLI TUI loop with menu

What would you like to do? (Press 'q' to quit)")
1 Add task")
2 Remove task")
3 Mark complete")
4 Display pending tasks")
5 Display completed tasks")
6 Save and quit")

#### Functions

1 load_from_file
arguments: 
    file: a .txt file path

function:
    check if file exists
    if it doesn't, create it
    if it does, read .txt file into a list format
    enumerate the list
    return the enumerated list object, called "tasks"
    
2 add_task
arguments:
    tasks: enumerated list of .txt file with lines of task strings

function:
    take user input for new task as string
    append user input to main tasks List
    return modified tasks list

3 remove_task
arguments:
    tasks: enumerated list of .txt file with lines of task strings

function:
    take user input of index # of task to remove
    pop() the task from tasks
    confirm poppedTask was removed
    re-enumerate tasks list
    write changes back to main tasks variable

4 mark_complete
arguments:
    tasks: main tasks list
    completed: list of completed tasks

functions:
    take user input for index of task to mark complete
    pop task from tasks
    append task to completed
    confirm task was marked as completed
    write changes to tasks and completed

5 display_content
arguments:
    user_content: tasks or completed objects

functions:
    check if list is more than PAGE_LENGTH long
    if not, for each task, prints the task number index and the task string
    if so, print PAGE_LENGTH - 5 tasks and prompt user for input 'n' to go to next page or 'q' to quit 

save_to_file
arguments:
    user_content: tasks or complted objects
    file: TASKS or COMPLETED file path

functions:
    checks that user_content is valid
    try to write user_content into file
    save file


