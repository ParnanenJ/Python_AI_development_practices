todo_list = []

while True:
  if not todo_list:
    print("Your ToDo list is empty")
  else:
    print("ToDo List:")
    index = 1
    for task in todo_list:
      print(f"{index}. {task}")
      index += 1

  print("Options:")
  print("1. Add Task")
  print("2. Remove Task")
  print("3. Quit")

  choice = input("Enter your choice (1, 2, or 3): ")

  if choice == "1":
    print("Adding task")
    new_task = input("Enter the task: ")
    todo_list.append(new_task)
    print(f"Task {new_task} added")
  elif choice == "2":
    remove_task = input("Choose task: ")
    if not todo_list:
      print("Your ToDo list is empty")
    else:
        if remove_task in todo_list:
            todo_list.remove(remove_task)
            print(f"Task {remove_task} removed")
        else:
            print(f"{remove_task} is not in the list.")
  elif choice == "3":
    print("Quitting")
    break
  else:
     print("Invalid choice, please enter 1, 2, or 3.")