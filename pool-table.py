import json
import datetime

class PoolTable:
    def __init__(self, number = 0, start = 0, end = 0, total_time = 0, occupied = False ):
        self.number = number
        self.start = ""
        self.end = ""
        self.total_time = ""
        self.occupied = occupie



#Empty array to save data
pool_tables = []

#JSON needs as dictionary
dict_tables = []

user_input = ""
#create 12 pool tables
def create_table():
    for i in range(1,13):
        pool_table = PoolTable(i)
        pool_tables.append(pool_table)
    for table in pool_tables:
        dict_tables.append(table.__dict__)
    save_pool_table()
    


#create main menu to display options
def main_menu():
    print("""Welcome to the University Center Game Room
    ~~~~~~~~~~~~~~~~~~~~~~~~
    Press 1 to view all tables
    Press 2 to open a table
    Press 3 to close a table
    Press q to quit
    """)


def view_all_tables():
    for table in dict_tables:
        print(table)


#work on renaming the file later! use f{name}
def save_pool_table():
    with open("today.json", "w") as file_object:
        json.dump(dict_tables, file_object)

def open_table():
    #append to the table_status array the time and table number
    #enter table number
    table = int(input("What table do you want to open? "))
    if table.occupied == False:
        table.start = get_time()
        table.occupied = True
    elif table.occupied == True:
        print("Please enter a different table number, this one is occupied")
    save_pool_table()



#Time the pool table will open/close
def get_time():
    time_now = datetime.datetime.now()
    format_time = time_now.strftime('%H:%M:%S')
    print(format_time)

def close_table():
    #if its the first table of the day, make a new json table
    table = input("What table do you want to close? ")
    if table.occupied ==True:
        table.end = get_time()
        table.occupied = False
    save_pool_table()

create_table()

while user_input != 'q':
    main_menu()
    if user_input == '1':
        view_all_tables()
    
    elif user_input == '2':
        open_table()
    
    elif user_input == '3':
        close_table()



