import json
import datetime

class PoolTable:
    def __init__(self, number = 0, start = 0, end = 0, total_time = 0, available = True):
        self.number = number
        self.start = ""
        self.end = ""
        self.total_time = ""
        self.available = True

    def TableInfo(self):
        return f"""
        Table Number: {self.number}
        Table Start Time: {self.start}
        Table End Time: {self.end}
        Total Time: {self.total_time}
        Is the table available?: {self.available}
        """


#empty array to save data
pool_tables = []

#JSON needs a dictionary
dict_tables = []

user_input = ""

#create 12 pool tables
for i in range(1, 13):
    table = PoolTable(str(i))
    dict_tables.append(table.__dict__)
    pool_tables.append(table)




def main_menu():
    print("""Welcome to the University Center Game Room
    ~~~~~~~~~~~~~~~~~~~~~~~~
    Press 1 to view all tables
    Press 2 to open a table
    Press 3 to close a table
    Press q to quit
    """)

def view_tables():
    for table in pool_tables:
        print(table.TableInfo())

#view_tables()

def check_out_table():
    table = int(input("What table number do you want to open? "))
    table_to_open = pool_tables[(table - 1)]
    if table_to_open.available == True:
        table_to_open.start = get_time()
        table_to_open.available = False
        print(table_to_open.TableInfo())
    elif table.available == False:
        print("Please enter a different table number: ")
    else: 
        print("Please enter a valid table option: ")

def get_time():
    time_now = datetime.datetime.now()
    format_time = time_now.strftime('%H:%M:%S')
    return format_time

def close_table():
    table = int(input("What table would you like to close? "))
    table_to_close = pool_tables[(table - 1)]
    if table_to_close.available == False:
        table_to_close.end = get_time()
        table_to_close.available = True
        #table_to_close.total_time = int(table_to_close.end) - int(table_to_close.start)
        print(table_to_close.TableInfo())
        with open("today.json", "w") as file_object:
            json.dump(dict_tables, file_object)
    elif table.available == True:
        print("Please enter a different table number to close: ")
    else:
        print("Please enter a valid table number: ")
    


while user_input != 'q':
    main_menu()
    user_input = input("What would you like to do? ")
    if user_input == '1':
        #View tables
        view_tables()
        
    elif user_input == '2':
        check_out_table()
        pass
    
    elif user_input == '3':
        #close table
        close_table()
    
    else:
        print("Please enter a valid choice")
    
