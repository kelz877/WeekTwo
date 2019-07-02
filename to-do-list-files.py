#saves the to do list into a file

#Welcome to the to do list
print("Welcome to your to do list")

#store each task in a dictionary. title and priority are keys

#store each dictionary inside an array. An array will represent a list of tasks


# when the app starts, give user a menu

def option_menu():
    print("""
    Press 1 to add a task
    Press 2 to delete a task
    Press 3 to view all tasks
    Press 4 to delete all tasks
    Press q to quit
    """)

#add task  -- > Ask user for title and priority
def add_task():

    with open("list.txt") as file_object:
        lines = file_object.readlines()

    title = input("What is the name of the task you have to do? ")
    priority = input("What is the priority? High, medium, or low? ")
    task = {
        "Title": title,
        "Priority": priority
    }
    #to_do_list.append(task)
    with open("list.txt", "a") as file_object:
        task_to_save = f'{len(lines) + 1} | {task["Title"]} | {task["Priority"]}\n'
        file_object.write(task_to_save)
        
#delete task
def delete_task():
    delete_item = input("Please enter the number of the item you would like to delete followed by a space: ")
    with open("list.txt") as file_object:
        lines = file_object.readlines()
    with open("list.txt", "w") as file_object:
        for line in lines:
            if not line.startswith(delete_item):
                file_object.write(line)

    #view_tasks()
    #delete_task = int(input("Enter the number of the task that you want to delete: "))
    #to_do_list

#view all tasks
def view_tasks():
    with open("list.txt", "r") as file_object:
        content = file_object.read()
        print(content)
        #for line in file_object:
            #print(line)

#delete everything in note
def delete_all_contents():
    print("""Are you sure that you want to delete the contents?
    If you do not wish to delete, exit the file by pressing
    CTRL-C (^C)
    """)
    input("?")
    file_object = open("list.txt", "w")
    file_object.truncate()



#empty user input
user_input = ""

#while loop for cycling the menu

while user_input != "q":
    option_menu()
    user_input = input("What would you like to do? ")

    if user_input == "1":
        add_task()

    elif user_input == "2":
        delete_task()

    elif user_input == "3":
        view_tasks()

    elif user_input == "4":
        delete_all_contents()


