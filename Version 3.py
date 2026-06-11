'''BDSC cafe program'''
'''This is a click and collect program that signs users' in using their
student ID, collects their orders and allows them to mark their order as completed'''

import sys, os
import tkinter as tk

#Dictionaries
login_keys = {}

#Import login details from external file into dictionary
with open("student_data.txt","r")as file: #With open, (read = r)
    for line in file:
        line = line.strip()#Removes spaces
        if line != "":
            id, pin  = line.split(":")
            login_keys[id] = int(pin)
            
#List in list to contain menu price
menu_prices = []

#Import menu details from external file into list
with open("cafe_menu.txt","r")as file: #With open, (read = r)
    for line in file:
        menu_item = []
        line = line.strip()#Removes spaces
        if line != "":
            item, price  = line.split(":")
            menu_item.append(item)
            menu_item.append(int(price))
            menu_prices.append(menu_item)


#Empty dictionary to store the ordered items
ordered_items = {}

#Empty list for users' previous orders
orders = []

#Initialise tkinter window
root = tk.Tk()
root.title("BDSC cafe")
root.geometry("550x300")

#Show frame function
def show_frame(frame):
    frame.tkraise()

#Creating different frames
welcome_frame = tk.Frame(root)
login_frame = tk.Frame(root)
home_frame = tk.Frame(root)
order_frame = tk.Frame(root)
currentorder_frame = tk.Frame(root)
menugallery_frame = tk.Frame(root)###

#Frame grids
welcome_frame.grid(row=0, column=0, sticky="nsew")
login_frame.grid(row=0, column=0, sticky="nsew")
home_frame.grid(row=0, column=0, sticky="nsew")
order_frame.grid(row=0, column=0, sticky="nsew")
currentorder_frame.grid(row=0, column=0, sticky="nsew")
menugallery_frame.grid(row=0, column=0, sticky="nsew")

#---------------Welcome screen---------------
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

#---------------Login screen---------------
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
                            fg="red"
                            )

loginerror_label.grid(row=4,
                      column=0,
                      )

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
        
#---------------Home screen---------------
#Home image
homeimage_path = "images/home_img.png"

homephoto = tk.PhotoImage(file=homeimage_path)

homeimage_label = tk.Label(home_frame,
                           image=homephoto)

homeimage_label.grid(row=0,
                     column=1,
                     rowspan=5,
                     padx=30)

#Successfully added order message
success_message = tk.StringVar()

success_label = tk.Label(home_frame,
                         textvariable=success_message,
                         fg="green")

success_label.grid(row=4,
                   column=0,
                   pady=10)

home_message = tk.Label(home_frame,
                           text = "Welcome home!")
order_option = tk.Button(home_frame,
                         text = "Order Menu",
                         command = lambda: [show_frame(order_frame),
                         success_message.set("")]
                         )# This message resets the success_message to "" so that the message disappears after entering a new frame)

currentorder_option = tk.Button(home_frame,
                         text = "View Current orders",
                         command = lambda: [view_current_orders(),
                         success_message.set("")]
                                )
gallery_option = tk.Button(home_frame,
                           text="View Menu Gallery",
                           command=lambda: [show_frame(menugallery_frame),
                           success_message.set("")])

home_message.grid(row=0, column=0, padx= 50, pady = 20)
order_option.grid(row=1, column= 0, padx= 50, pady = 20)
currentorder_option.grid(row=2, column=0 , padx= 50, pady = 20)
gallery_option.grid(row=3, column=0 , padx= 50, pady = 20)


#---------------Menu gallery screen---------------

#Gallery scrollbar
#scrollbar canvas
scroll_canvas = tk.Canvas(menugallery_frame,
                          width=200)

scroll_canvas.pack(side="left",
                   fill="both",
                   expand=True,)

#Scrollbar syntax
scrollbar = tk.Scrollbar(menugallery_frame,
                orient="vertical",
                command=scroll_canvas.yview) #.yview moves the canvas when scrollbar is dragged)
#Place scrollbar on the right side
scrollbar.pack(side="right",
               fill="y")

scroll_canvas.configure(yscrollcommand=scrollbar.set)

#Frame to hold the scroll container
gallery_frame = tk.Frame(scroll_canvas)

gallery_frame.bind(
    "<Configure>",
    #bbox("all") gets the size of everything inside canvas
    lambda e: scroll_canvas.configure(
        scrollregion=scroll_canvas.bbox("all")
    )
)
#Put the gallery frame into the canvas
scroll_canvas.create_window((0,0),#(0,0) = top left corner
                            window=gallery_frame,
                            anchor="nw")#anchor="nw" means top-left alignment


for i, image_file in enumerate(os.listdir("food_images")):
    
    image_path = f"food_images/{image_file}"
    photo = tk.PhotoImage(file=image_path)
    item_name = image_file.replace(".png", "")
    item_label = tk.Label(gallery_frame,
                          text=item_name) 
    item_label.grid(row=i*2,
                    column=0,
                    padx=100,
                    pady=20,)
    image_label = tk.Label(gallery_frame,
                           image=photo)
    image_label.image = photo
    image_label.grid(row=i*2+1,
                     column=0)
#Home button
galleryhome_button = tk.Button(gallery_frame,
                    text="\nRETURN HOME\n",
                    command=lambda: show_frame(home_frame),
                    )

galleryhome_button.grid(row=1,
                column=2,
                padx=20,
                pady=0,
                      )


#---------------Order screen---------------

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
    price_label = tk.Label(order_frame,
                           text=f"${price}")
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
    total_price = 0
    
    for item, var in ordered_items.items():
        quantity = var.get()
        if quantity > 0:
            #Append item string name multiplied by quantity selected
            cart.append(f"{item} x{quantity}")
            
            #Add item prices multiplied by quantity
            for menu_item, price in menu_prices:
                if menu_item == item:
                    total_price += price * quantity

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
            file.write(f"- {item}\n")#This prints the items in the cart and the quantity
        file.write(f"STATUS: Preparing\n")
        file.write(f"TOTAL: ${total_price}\n")
        file.write(f"-----------------------\n\n")
        
        order_number+=1
        with open("order_number.txt", "w") as file:
            file.write(str(order_number))
            cart.clear()
        #Make the success message on the home frame appear
        success_message.set("Order successfully added!")
                
                
    
    #After the ordering process has finished, the user returns to the home frame   
    show_frame(home_frame)
    
#Home button
orderhome_button = tk.Button(order_frame,
                    text="\nRETURN HOME\n",
                    command=lambda: show_frame(home_frame),
                    )

orderhome_button.grid(row=2,
                column=3,
                padx=20,
                pady=0,
                      )

    
#---------------Current order screen---------------

#Current order Scrollbar
#scrollbar canvas
orderscroll_canvas = tk.Canvas(currentorder_frame,
                            width=500)
orderscroll_canvas.pack(side="left",
                    fill="both",
                    expand=True,)

#Scrollbar syntax
orderscrollbar = tk.Scrollbar(currentorder_frame,
                orient="vertical",
                command=orderscroll_canvas.yview) #.yview moves the canvas when scrollbar is dragged)
#Place scrollbar on the right side
orderscrollbar.pack(side="right",
                fill="y")

orderscroll_canvas.configure(yscrollcommand=orderscrollbar.set)

#Frame to hold the scroll container
current_frame = tk.Frame(orderscroll_canvas)

current_frame.bind(
    "<Configure>",
    #bbox("all") gets the size of everything inside canvas
    lambda e: orderscroll_canvas.configure(
        scrollregion=orderscroll_canvas.bbox("all")
    )
)
#Put the gallery frame into the canvas
orderscroll_canvas.create_window((0,0),#(0,0) = top left corner
                            window=current_frame,
                            anchor="nw")#anchor="nw" means top-left alignment

def view_current_orders():
    #Set row number to 0
    row_num = 0

    #Initially, no previous orders were found
    orders_found = False
    
    show_frame(currentorder_frame)

    #Clear old widgets INSIDE the scrolling frame
    for widget in current_frame.winfo_children():
        widget.destroy()

    #Home button
    crntordhome_button = tk.Button(
        current_frame,
        text="\nRETURN HOME\n",
        command=lambda: show_frame(home_frame)
    )

    crntordhome_button.grid(row=0,
                            column=3,
                            padx=5,
                            pady=20)
    #Find current orders
    for file_name in os.listdir():
        if user_id in file_name:

            with open(file_name, "r") as file:
                current_order = file.read()
                orders_found = True

            #Order invoice label
            order_invoice = tk.Label(
                current_frame,
                text=current_order
            )
            order_invoice.grid(row=row_num,
                               column=0,
                               padx=10,
                               pady=5)
            #Status setup
            status = ""

            if "Preparing" in current_order:
                status = "Preparing"
                colour = "orange"

            if "Ready" in current_order:
                status = "Pick up now!"
                colour = "green"
            #Status label
            status_label = tk.Label(
                current_frame,
                text=status,
                fg=colour
            )
            status_label.grid(row=row_num,
                              column=1,
                              padx=2,
                              pady=5)
            #Completed button
            completed_button = tk.Button(
                current_frame,
                text="Mark as Completed",
                command=lambda file=file_name: remove_order(file)
            )
            completed_button.grid(row=row_num,
                                  column=2,
                                  padx=20,
                                  pady=5)

            row_num += 1
    #If no orders found
    if orders_found == False:

        no_orders_label = tk.Label(
            current_frame,
            text="No orders to display"
        )

        no_orders_label.grid(row=0,
                             column=0,
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
