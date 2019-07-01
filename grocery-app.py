


class ShoppingList:
  def __init__(self, name, address):
    self.name = name
    self.address = address
    self.grocery_items = []

class GroceryItem:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity


#Create a grocery list application
print("Hello and welcome to your grocery lists")

#create an empty array to store the names of shops
shopping_lists = []

#assign the user input as an empty String
user_input = ""

#Function to display the menu
def display_menu():
  print("""
  Press 1 to add a new list for a grocery store   
  Press 2 to view your saved lists
  Press 3 to add items to one of your lists
  Press 4 to view the items on a list
  Press q to quit your grocery list app!
  """)


#function to view all lists 
def view_list():
  for index in range(0, len(shopping_lists)):
    print(f"{index + 1} - {shopping_lists[index].name}")

def add_to_list():
  name = input("What is the name of the store you are shopping at? ")
  address = input("What is the address of the store? ")
  name_address = ShoppingList(name, address)
  shopping_lists.append(name_address)
  #print(shopping_lists)

def list_to_add_to():
  #Enter the list number you want to add items to
  shopping_list_number = int(input("Enter the shopping list you would like to add items to: "))
  shopping_list_to_add_items = shopping_lists[shopping_list_number - 1]
  item_name = input("Enter the name of the item: ")
  item_price = float(input("Enter the cost of the item: "))
  item_quantity = int(input("Enter the quantity of the item: "))
  grocery_item = GroceryItem(item_name, item_price, item_quantity)
  shopping_list_to_add_items.grocery_items.append(grocery_item)
  print(f"Item name: {item_name} -- Item Price: ${item_price} -- Quantity of Item: {item_quantity} --")






while user_input != "q":
    #print all of the options at once for the User 
  display_menu()
  user_input = input("What would you like to do?")

  if user_input == "1":
    add_to_list()

  elif user_input == "2":
    view_list()
  
  elif user_input == "3":
    view_list()
    list_to_add_to()
  
  else:
      print("Please enter a valid input")
 





    