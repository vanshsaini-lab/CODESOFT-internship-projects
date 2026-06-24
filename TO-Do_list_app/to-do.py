import json
print("\n\n")

print("=========================== Welcome to Your TO-DO list app ========================================")

try:
    with open("tasks.json","r") as file:      
        tasks = json.load(file)             # loads data if file already exist
except FileNotFoundError:
    tasks=[]                                #creates an empty file 

# save function to save tasks in a file
def save_tasks():
    with open ("tasks.json","w") as file:
        json.dump(tasks,file,indent=4)


# To create a TO-DO list
if not tasks:
    tsk_num = int(input("Enter no. of tasks you want to add: "))

    for i in range(tsk_num):
        tsk_name = input(f"enter task {i+1}: ")
        tasks.append({
            'task': tsk_name,
            'completed': False
        })

save_tasks()
print("\n")

print("Your TO-DO list: ")
# prints complete list
for i, task in enumerate(tasks, start=1):
            status = "[DONE]" if task["completed"] else "[ ]"
            print(f"{i}. {status} {task['task']}\n")

print("---------------------------------------------------------------------------------------------------")
while True:
    print("select what you want to do : \n")
    try:
        choice = int(input(
        "1. ADD a task\n" 
        "2. DELETE a task\n"
        "3. UPDATE a task\n"
        "4. MARK task as completed\n"
        "5. VIEW all tasks\n"
        "6. EXIT/STOP\n"
        "Enter number of the task you want to do : "
         ))
    except ValueError:
        print("Enter a number !")
        continue
    print("---------------------------------------------------------------------------------------------------")
# to add a task in the list
    if choice == 1:
        tsk_name = input("Enter task: ")
        tasks.append({'task': tsk_name, 'completed': False})
        print("Task added successfully!")
        save_tasks()
        print("---------------------------------------------------------------------------------------------------")

#to delete task from the list
    elif choice == 2:
        try:
            tsk_num = int(input("Enter Task no. to delete: "))
            if 1<= tsk_num <= len(tasks):
                tasks.pop(tsk_num-1)
                print("task DELETED sucessfully!")
            else:
                print("Enter task number!")
        except ValueError:
            print("enter a number !")
            continue
        save_tasks()
        print("---------------------------------------------------------------------------------------------------")

#to update a task from the list
    elif choice == 3:
        tsk_name = input("Enter Task to update: ")
        # find task by name and update its 'task' value
        for task in tasks:
            if task['task'] == tsk_name:
                up_tsk = input("Enter NEW task : ")
                task['task'] = up_tsk
                print(f"{tsk_name} Updated successfully!")
                break
        else:
            print(f"{tsk_name} not found")
        save_tasks()
        print("---------------------------------------------------------------------------------------------------")
#to mark a task as done 
    elif choice == 4 :
        

        for i, task in enumerate(tasks, start=1):
            status = "[DONE]" if task["completed"] else "[ ]"
            print(f"{i}. {status} {task['task']}")
        try:
            task_num = int(input("Enter task number: "))
        except ValueError:
            print("Enter Valid Number !")
            continue

        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number!")
        print("---------------------------------------------------------------------------------------------------")
        save_tasks()
#to view the complete to-do list        
    elif choice == 5 :
        print("Your TO-DO list: \n")
        for i, task in enumerate(tasks, start=1):
            status = "[DONE]" if task["completed"] else "[ ]"
            print(f"{i}. {status} {task['task']}\n")
        print("---------------------------------------------------------------------------------------------------")
        print("\n")

#to exit from the app   
    elif choice == 6:
        print("Saved Sucessfully!")
        save_tasks()
        print("---------------------------------------------------------------------------------------------------")
        break


    else:
        print("INVALID CHOICE!")
   

