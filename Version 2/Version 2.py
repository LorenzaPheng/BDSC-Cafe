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

#Empty dictionary to store the ordered items
ordered_items = {}

#Empty list for users' previous orders
orders = []

#Initialise tkinter window
root = tk.Tk()
root.title("BDSC cafe")
root.geometry("500x300")

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
    global user_id
    #Empty variable for user id
    user_id = ""
    try:

        entered_id = id_entry.get()
        entered_pin = int(pin_entry.get())

        if entered_id not in login_keys:

            loginerror_message.set("ID not found")

        elif entered_pin == login_keys[entered_id]:

            loginerror_message.set("")
            show_frame(home_frame)
            user_id = entered_id

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
                         command = lambda: view_current_orders())

home_message.grid(row=0, column=0, padx= 50, pady = 20)
order_option.grid(row=1, column= 0, padx= 50, pady = 20)
currentorder_option.grid(row=2, column=0 , padx= 50, pady = 20)

#Order screen

#Spinboxes for option selection

for i, (item, price) in enumerate(menu_prices):
    #Item labels
    item_label = tk.Label(order_frame,
                          text=item,)
    item_label.grid(row = i+1, #the row increases for each item
                    column=0,
                    padx=20,
                    pady=5,
                    )
    #Price labels
    price_label = tk.Label(order_frame, text=price)
    price_label.grid(row=i+1,
                     column=1,
                     padx=10,
                     pady=5,)

    #Generate spinboxes for menu items
    sb_var = tk.IntVar(value=0) #IntVar carries the value of the spinbox
    item_spinbox = tk.Spinbox(order_frame,
                              from_=0, to=10,
                              width=5,
                              textvariable=sb_var)
    item_spinbox.grid(row=i+1,
                      column=2,
                      padx=20,
                      pady=5)
    
    ordered_items[item] = sb_var

#Button to confirm order
order_button = tk.Button(order_frame,
                        text = "Add to cart",
                        command = lambda:add_order(),
                             )
order_button.grid(row=len(menu_prices)+1,
                    column=0,
                    pady=20,
                    padx=10)

#Function to add orders
def add_order():
    global cart
    cart = []
    for item, var in ordered_items.items():
        quantity = var.get()
        if quantity > 0:
            # Append item string name multiplied by quantity selected
            cart.append(f"{item} x{quantity}")
    
    if len(cart) == 0:
        return #If user has no orders to display, return them to the main_frame
            
    with open("order_number.txt", "r") as file:
        order_number = int(file.read())
                            
    with open(f"{user_id}_order_{order_number}.txt", "x") as file:
        file.write(f"---BDSC CAFE ORDER {order_number}---\n")
        file.write(f"Student ID: {user_id}\n")
        file.write(f"-----------------------\n")
        file.write(f"Items Ordered:\n")
        for item in cart:
            file.write(f"- {item}\n")
        file.write(f"Status: Preparing\n")
        file.write(f"-----------------------\n\n")
                            
        order_number+=1
        with open("order_number.txt", "w") as file:
            file.write(str(order_number))
            cart.clear()
                
                
    
    #After the ordering process has finished, the user returns to the home frame   
    show_frame(home_frame)
    
#Home button
orderhome_button = tk.Button(order_frame,
                    text="\nRETURN HOME\n",
                    command=lambda: show_frame(home_frame))

orderhome_button.grid(row=1,
                column=3,
                padx=20,
                pady=20)

    
#Current order screen

def view_current_orders():
    #Set row number to 0
    row_num = 0

    #Inititally, no previous orders were found for the user
    orders_found = False
    
    show_frame(currentorder_frame)

    #Reset current orders every time you open it 
    for widget in currentorder_frame.winfo_children():
        widget.destroy()
        
    #create home button
    crntordhome_button = tk.Button(currentorder_frame,
                            text="\nRETURN HOME\n",
                            command=lambda: show_frame(home_frame))

    crntordhome_button.grid(row=0,
                     column=2,
                     padx=20,
                     pady=20)

    #Find any current orders for the user's id
    for file_name in os.listdir():
        if user_id in file_name:
            with open(file_name, "r") as file:
                current_order = file.read()
                orders_found = True #User id has been found
                
            order_invoice = tk.Label(currentorder_frame,
                                    text=current_order)
            order_invoice.grid(row = row_num,
                            column = 0,
                            padx =20,
                            pady=5,
                            )
            
            completed_button = tk.Button(currentorder_frame,
                                text="Mark as Completed",
                                command=lambda file=file_name: remove_order(file)
                                )
            completed_button.grid(row=row_num,
                                    column=1,
                                    padx=20,
                                    pady=5)

            row_num += 1

#If no orders have been found
        if orders_found == False:
            no_orders_label = tk.Label(currentorder_frame,
                                       text = "No orders to display",
                                       )
            no_orders_label.grid(row = 0,
                                 column = 0,
                                 padx=20,
                                 pady=5)

#Function to remove order from file
def remove_order(file):
    os.remove(file)
    view_current_orders()

# Show welcome screen first
show_frame(welcome_frame) 

# Run the program
root.mainloop()               
