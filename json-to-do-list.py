import json

#empty array to hold data
to_do_list = []


#user main menu of options

main_menu = print("""
Press 1 to add an item to your list
Press 2 to delete an item
Press 3 to view all items
Press 4 to qiut
""")

#Ask the user for the 'title' and 'priority' of the task. Priority can be high, medium and low. 
def add_task():
    title = input("What is the name of your task?" )
    priority = input("Is the priority high, medium, or low? " )
    task_dict = {"Title": title, "Priority": priority}
    to_do_list.append(task_dict)
    with open("list_items.json", "w") as file_object:
        json.dump(to_do_list, file_object)



#Show user all the tasks along with the index number of each task. 
# User can then enter the index number of the task to delete the task. 
def delete_task():
    #view the list first
    view_list()
    delete_item = int(input("What is the number of the task you wish to delete? "))
    #to_do_list.pop(delete_item - 1)
    del to_do_list[delete_item - 1]
    with open("list_items.json", "w") as file_object:
        json.dump(to_do_list, file_object)



#allow the user to view tasks in the following format
# 1 - Wash the car - High

def view_list():
    for index in range(0, len(to_do_list)):
        print(f"{index + 1} - {to_do_list[index]['Title']} - {to_do_list[index]['Priority']}")


user_input = ""

while user_input != "q":
    main_menu
    user_input = input("What would you like to do? " )

    if user_input == "1":
        add_task()

    elif user_input == "2":
        delete_task()
    
    elif user_input == "3":
        view_list()



