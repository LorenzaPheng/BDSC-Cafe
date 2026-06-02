'''BDSC cafe program'''
'''This is a click and collect program that signs users' in using their
student ID, collects their orders and allows them to mark their order as completed'''

import sys, os
import tkinter as tk

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
menu_items = ["Chocolate milk", "Sausage roll", "Brownie"]

#Empty list for users' ordered items
cart = []
    
#Empty variable for user id
user_id = ""

#Initialise tkinter window
root = tk.Tk()
root.title("BDSC cafe")
root.geometry("400x300")

#Show frame function
def show_frame(frame):
    frame.tkraise()

#Creating different frames
welcome_frame = tk.Frame(root)
login_frame = tk.Frame(root)
home_frame = tk.Frame(root)
order_frame = tk.Frame(root)
currentorder_frame = tk.Frame(root)

#Frame grids
welcome_frame.grid(row=0, column=0, sticky="nsew")
login_frame.grid(row=0, column=0, sticky="nsew")
home_frame.grid(row=0, column=0, sticky="nsew")
order_frame.grid(row=0, column=0, sticky="nsew")
currentorder_frame.grid(row=0, column=0, sticky="nsew")

#Welcome screen
title = tk.Label(welcome_frame,
                 text = "Welcome to the BDSC cafe app!")
title.grid(row=0, column = 0, pady = 20, padx = 60)
welcome_message = tk.Label(welcome_frame,
                           text = "Simply click and collect!",
                           font = ("Arial", 9))
welcome_message.grid(row = 1, column = 0, pady = 20, padx = 60)
login_button = tk.Button(welcome_frame,
                         text = "Log in",
                         command = lambda: show_frame(login_frame))
login_button.grid(row = 2, column = 0, pady = 20, padx = 60)

#Login screen
login_instruction = tk.Label(login_frame,
                             text = "Enter student ID and PIN",
                             font = ("Arial, 12"),
                             )
login_instruction.grid(row=0, column = 0, pady = 20, padx = 30)
#ID entrybox
id_label = tk.Label(login_frame,
                    text = "Student ID : ",
                    font = ("Arial", 9))
id_label.grid(row = 1, column = 0)
id_entry = tk.Entry(login_frame)
id_entry.grid(row = 1, column = 1)
#PIN entrybox
pin_label = tk.Label(login_frame,
                    text = "PIN : ",
                    font = ("Arial", 9))
pin_label.grid(row = 2, column = 0)
pin_entry = tk.Entry(login_frame)
pin_entry.grid(row = 2, column = 1, pady = 40,)
#Enter login details button
enter_button = tk.Button(login_frame,
                         text = "Enter",
                         command = lambda: verify_user())
enter_button.grid(row = 3, column = 0, pady = 10,)

loginerror_message = tk.StringVar()
loginerror_label = tk.Label(login_frame,
                            textvariable=loginerror_message,
                            )

loginerror_label.grid(row=4, column=0)

#Login verification process
def verify_user():

    try:

        entered_id = id_entry.get()
        entered_pin = int(pin_entry.get())

        if entered_id not in login_keys:

            loginerror_message.set("ID not found")

        elif entered_pin == login_keys[entered_id]:

            loginerror_message.set("")
            show_frame(home_frame)

        else:

            loginerror_message.set("ID or PIN is incorrect")

    except ValueError:

        loginerror_message.set("Enter valid ID and PIN in integers")
            
#Home screen
home_message = tk.Label(home_frame,
                           text = "Welcome home!")
order_option = tk.Button(home_frame,
                         text = "Order Menu",
                         command = lambda: show_frame(order_frame))
currentorder_option = tk.Button(home_frame,
                         text = "View Current orders",
                         command = lambda: show_frame(order_frame))

home_message.grid(row=0, column=0, padx= 50, pady = 20)
order_option.grid(row=1, column= 0, padx= 50, pady = 20)
currentorder_option.grid(row=2, column=0 , padx= 50, pady = 20)

#Order screen

#Spinboxes for option selection

for item in menu_items:
    item_label = tk.Label(order_frame,
                          text=item,)
    item.label.grid(row = i+1, #the row increases for each item
                    column=0,
                    padx=20,
                    pady=5,
                    )

    #Generate spinboxes for menu items
    sb_var = tk.IntVar(value=0) #IntVar carries the value of the spinbox
    item_spinbox = tk.Spinbox(order_frame,
                              from_=0, to=10,
                              width=5,
                              textvariable=sb_var)
    item_spinbox.grid(row=i+1,
                      column=1,
                      padx=20,
                      pady=5)
    
    

#Function to add orders
def add_order():
    cart.append(menu.spinbox.get())
    show_frame(home_frame)
    
'''#Variable for the selected food item to be stored to
food_choice = tk.IntVar()

order_instruction = tk.Label(order_frame,
                             text = "Tick all the items you want to order!")
order_instruction.grid(row = 0, column = 0, padx= 50, pady = 20)

chocolate_milk = tk.Radiobutton(order_frame,
                                text="Chocolate milk",
                                variable=food_choice,
                                value=1)

sausage_roll = tk.Radiobutton(order_frame,
                              text="Sausage roll",
                              variable=food_choice,
                              value=2)

brownie = tk.Radiobutton(order_frame,
                         text="Brownie",
                         variable=food_choice,
                         value=3)

chocolate_milk.grid(row=1,column=0)
sausage_roll.grid(row=2,column=0)
brownie.grid(row=3,column=0)

order_button = tk.Button(order_frame,
                         text = "Order",
                         command = lambda: add_order)
order_button.grid(row=4,column=0, padx= 50, pady = 20)

#Add order function
def add_order():

    selected = food_choice.get()

    if selected == 1:
        cart.append("Chocolate milk")

    elif selected == 2:
        cart.append("Sausage roll")

    elif selected == 3:
        cart.append("Brownie")'''
        
#Current order screen

# Show welcome screen first
show_frame(welcome_frame) 

# Run the program
root.mainloop()       
            
            
        
        

"""
#Main menu- Selecting option
def main_menu():

    print("\n--------MAIN MENU--------\n")
    print("OPTIONS:")
    print("1. Order Menu")
    print("2. Current orders")
    print("3. Exit")

    while True:
        try:
            choice = int(input("Enter option (1/2/3) : "))
            if choice == 1:
                order_menu()
            elif choice == 2:
                current_orders()
            elif choice == 3:
                print("\n--------EXITING PROGRAM--------")
                sys.exit()
        except ValueError:
            print("Invalid option")
            
        
#Order menu - Place an order
def order_menu():
    global order_number
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
                with open("order_number.txt", "r") as file:
                    order_number = int(file.read())
                    
                with open(f"{user_id}_order_{order_number}.txt", "x") as file:
                    file.write(f"---BDSC CAFE ORDER {order_number}---\n")
                    file.write(f"Student ID: {user_id}\n")
                    file.write(f"-----------------------\n")
                    file.write(f"Items Ordered:\n")
                    for item in cart:
                        file.write(f"- {item}\n")
                    file.write(f"-----------------------\n\n")
                    
                    order_number+=1
                    with open("order_number.txt", "w") as file:
                        file.write(str(order_number))
                cart.clear()
                
            main_menu()
            break
            
        else:
            print("Enter a valid menu number in integers")        

#Current orders functions
def current_orders():
    
    #Empty list for users previous orders
    found_orders = []
    
    #Initially, previous orders are not found
    order_found = False
    
    print("\n--------CURRENT ORDERS--------\n")
    
    #Find any current orders for the user's id
    for file_name in os.listdir():
        if user_id in file_name:
            with open(file_name, "r") as file:
                current_order = file.read()
                found_orders.append(file_name)
                print(current_order)
            order_found = True
            
    if order_found == False:
        print("No current orders")
            
    else:
        while True:
            status = input("Have you recieved your order yet? (Y/N) : ").lower()
            if status == "y":
                print("Enjoy!")
                for file_name in found_orders:
                    os.remove(file_name)
                break
            if status == "n":
                print("Your order will be ready soon!")
                break
            else:
                print("Enter a valid status (Y/N)") 
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
"""
