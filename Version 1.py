'''BDSC cafe program'''
'''This is a click and collect program that signs users' in using their
student ID, collects their orders and allows them to mark their order as completed'''

import sys

#Dictionaries
login_keys = {
    "23419" : 9837,
    "23451" : 7654,
    "23444" : 7777
              }

menu_prices = [
    ["Chocolate milk", "$3"],
    ["Sausage roll", "$4"],
    ["Brownie", "$2"]
]

#Empty list for users' ordered items
cart = []

#Empty variable for user id
user_id = ""

#Main menu - Selecting option
def main_menu():

    print("\n--------MAIN MENU--------\n")
    print("OPTIONS:")
    print("1. Order Menu")
    print("2. Current orders")
    print("3. Exit")

    while True:
        choice = int(input("Enter option (1/2/3) : "))
        if choice == 1:
            order_menu()
        if choice == 2:
            current_orders()
        if choice == 3:
            print("\n--------EXITING PROGRAM--------")
            sys.exit()
        else:
            print("Invalid option")
        
#Order menu - Place an order
def order_menu():
    print("\n--------ORDER MENU--------")

    for index, (item, price) in enumerate(menu_prices, start=1):
        print(f"{index}. {item} : {price}")
    while True:
        try:
            ordered_item = int(input("Enter number to order or type '0' to stop : "))
        except ValueError:
            print("Enter a valid menu number in integers")
            continue
        
        if 1 <= ordered_item <= len(menu_prices):
            
            #Retrieves item name from the list by getting index number
            item_name = menu_prices[ordered_item - 1]
            cart.append(item_name)
            print("Successfully added to cart!")
            
        elif ordered_item == 0:

            if len(cart) == 0:
                main_menu()
                break
            else:
                print("\nOrder processed!\n")
                with open("current_orders.txt", "a") as file:
                    file.write(f"--- BDSC CAFE ORDER ---\n")
                    file.write(f"Student ID: {user_id}\n")
                    file.write(f"-----------------------\n")
                    file.write(f"Items Ordered:\n")
                    for item in cart:
                        file.write(f"- {item}\n")
                    file.write(f"-----------------------\n\n")
            main_menu()
            break
            
        else:
            print("Enter a valid menu number in integers")        

#Current orders functions
def current_orders():

    print("\n--------CURRENT ORDERS--------")

    if len(cart) == 0:
        print("No current orders")
        main_menu()
    else:
        print(cart)
        with open("tutor_list.txt","r")as file: 
            for line in file:
            line = line.strip()
        if line != "":
        main_menu()

#Initial menu - Logging in
def log_in():
    global user_id
    print("--------LOG IN--------")
    while True:
        entered_id = input("Enter student ID : ")
        if entered_id not in login_keys:
            print("ID not found")
        else:
            try:
                entered_pin = int(input("Enter PIN : "))
                if entered_pin == login_keys[entered_id]:
                    user_id = entered_id
                    print("--------SUCCESSFULLY LOGGING IN--------")
                    main_menu()
                    break
                else:
                    print("PIN OR ID IS INCORRECT")
            except ValueError:
                print("Enter a valid PIN in integers")
log_in()
