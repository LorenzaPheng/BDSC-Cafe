'''BDSC cafe program'''
'''This is a click and collect program that signs users' in using their
student ID, collects their orders and allows them to mark their order as completed'''
#---------------IMPORTS---------------
# os is used for file handling and finding order files
# tkinter is used to create the GUI
# messagebox is used to display pop-up messages
# ttk is used for themed widgets such as scrollbars
import sys, os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

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
root.geometry("550x350")
root.configure(bg="#5b183a")

#Show frame function
def show_frame(frame):
    frame.tkraise()

#Creating different frames
welcome_frame = tk.Frame(root,
                         bg = "#5b183a",)
login_frame = tk.Frame(root,
                       bg = "#5b183a",)
home_frame = tk.Frame(root,
                      bg = "#5b183a",)
order_frame = tk.Frame(root,
                       bg = "#5b183a",)
currentorder_frame = tk.Frame(root,
                       bg = "#5b183a",)
menugallery_frame = tk.Frame(root,
                       bg = "#5b183a",)
help_frame = tk.Frame(root,
                       bg = "#5b183a",)

#Frame grids
welcome_frame.grid(row=0, column=0, sticky="nsew",)
login_frame.grid(row=0, column=0, sticky="nsew")
home_frame.grid(row=0, column=0, sticky="nsew")
order_frame.grid(row=0, column=0, sticky="nsew")
currentorder_frame.grid(row=0, column=0, sticky="nsew")
menugallery_frame.grid(row=0, column=0, sticky="nsew")
help_frame.grid(row=0, column=0, sticky="nsew")

#---------------Welcome screen---------------
#logo image
logoimage_path = "images/logo.png"

logophoto = tk.PhotoImage(file=logoimage_path)

logoimage_label = tk.Label(welcome_frame,
                           image=logophoto,
                           bg = "#5b183a",)

logoimage_label.grid(row=0,
                     column=0,
                     padx=30,
                     pady=10)
#Welcome Title
title = tk.Label(welcome_frame,
                 text = "Welcome to the BDSC cafe app!",
                 font = "Times 20 bold",
                 bg = "#5b183a",
                 fg = "white",)
title.grid(row=1, column = 0, pady = 20, padx = 60)

#Welcome slogan
welcome_message = tk.Label(welcome_frame,
                           text = "Simply click and collect!",
                           font = ("Arial", 9),
                           bg = "#5b183a",
                           fg = "white",)
welcome_message.grid(row = 2, column = 0, pady = 20, padx = 60)

#Login button
login_button = tk.Button(welcome_frame,
                         text = "Log in",
                         bg = "#5b183a",
                         fg = "white",
                         command = lambda: show_frame(login_frame))

login_button.grid(row = 3, column = 0, pady = 5, padx = 60,
                  )
#Exit program function
def exit_program():
    root.destroy()
#Exit program button
welcome_exit=tk.Button(welcome_frame,
                       text="Exit program",
                       bg = "#5b183a",
                       fg = "white",
                       command=lambda:exit_program(),)
welcome_exit.grid(row = 4, column = 0, pady = 5, padx = 60,
                  )
    

#---------------Login screen---------------

#Main menu button
login_mmbutton=tk.Button(login_frame,
                         text="Main Menu",
                         bg = "#5b183a",
                         fg= "white",
                         command=lambda:show_frame(welcome_frame))

login_mmbutton.grid(row = 4,
                    column=2,)
#Login prompt
login_instruction = tk.Label(login_frame,
                             text = "Enter student ID and PIN",
                             font = "Times 15 bold",
                             bg = "#5b183a",
                             fg= "white",
                             )
login_instruction.grid(row=0, column = 0, pady = 20, padx = 30)
#ID entrybox
id_label = tk.Label(login_frame,
                    text = "Student ID : ",
                    font = ("Arial", 9),
                    bg = "#5b183a",
                    fg= "white",)
id_label.grid(row = 1, column = 0)
id_entry = tk.Entry(login_frame)
id_entry.grid(row = 1, column = 1)
#PIN entrybox
pin_label = tk.Label(login_frame,
                    text = "PIN : ",
                    font = ("Arial", 9),
                    bg = "#5b183a",
                    fg= "white",)
pin_label.grid(row = 2, column = 0)
pin_entry = tk.Entry(login_frame)
pin_entry.grid(row = 2, column = 1, pady = 40,)
#Enter login details button
enter_button = tk.Button(login_frame,
                         text = "Enter",
                         command = lambda: verify_user(),
                         bg = "#5b183a",
                         fg= "white",)
enter_button.grid(row = 3, column = 0, pady = 10,)

#Login error message variable
loginerror_message = tk.StringVar()
loginerror_label = tk.Label(login_frame,
                            textvariable=loginerror_message,
                            fg="#f05348",
                            bg = "#5b183a",
                            )

loginerror_label.grid(row=4,
                      column=0,
                      )
#logo image

croplogoimage_path = "images/crop_logo.png"

croplogophoto = tk.PhotoImage(file=croplogoimage_path)

loginlogoimage_label = tk.Label(login_frame,
                           image=croplogophoto,
                                bg = "#5b183a",)

loginlogoimage_label.grid(row=3,
                     column=2,
                     padx=30,
                     pady=10)


#Login verification process
def verify_user():
    global user_id
    #Empty variable for user id
    user_id = ""
    try:

        entered_id = id_entry.get()
        entered_pin = int(pin_entry.get())

        if entered_id not in login_keys:
            #Set the loginerror message depending on error
            loginerror_message.set("ID not found")

        elif entered_pin == login_keys[entered_id]:

            loginerror_message.set("")
            show_frame(home_frame)
            user_id = entered_id
            
            #Clear both entry fields completely
            id_entry.delete(0, tk.END)
            pin_entry.delete(0, tk.END)

            messagebox.showinfo("Success","Successfully logged in!") 

        else:
            #Set the loginerror message depending on error
            loginerror_message.set("ID or PIN is incorrect")

    #Set the loginerror message depending on error
    except ValueError:
        loginerror_message.set("Enter valid ID and PIN in integers")
        
#---------------Help screen---------------
#Title of help screen
helptitle = tk.Label(help_frame,
                 text = "Instructions Menu",
                 font = "Times 20 bold",
                 bg = "#5b183a",
                 fg = "white",)
helptitle.grid(row=0,
               column=1,
               padx=10,
               pady=10,)
#Instructions label
instructions = tk.Label(help_frame,
                text="1. Place an order\n2. Tap 'current orders'\n3. Wait until your order status is 'Ready'\n4. Collect your order from the cafe!",
                font = "Arial 15",
                bg = "#5b183a",
                fg = "white",
                )
                
instructions.grid(row=1,
                  column=1,
                  padx=10,
                pady=20,)
#Contact details

instructionshelp = tk.Label(help_frame,
                text="Need help? Contact :",
                font = "Arial 14 bold",
                bg = "#5b183a",
                fg = "#c2bdae",
                )
#Email image and label

emailimage_path="images/mail.png"
emailphoto = tk.PhotoImage(file=emailimage_path)
emailimage =tk.Label(help_frame,
                    text="cafe@bdsc.school.nz",
                    compound = "left",
                    font = "Arial 14",
                    bg = "#5b183a",
                    fg = "#c2bdae",
                    image = emailphoto,
                    padx=10,)
emailimage.grid(row=3,
                column=1,
                )

#Phone number image and label

phoneimage_path="images/phone.png"
phonephoto = tk.PhotoImage(file=phoneimage_path)

phonelabel= tk.Label(help_frame,
                text="273-2310 ext. #251",
                font = "Arial 14",
                bg = "#5b183a",
                fg = "#c2bdae",
                compound = "left",
                padx=10,
                image=phonephoto
                )

phonelabel.grid(row=4,
                column=1,  
                )

instructionshelp.grid(row=2,
                  column=1,
                  padx=10,
                  pady=5,)

#Home button
instruction_home = tk.Button(help_frame,
                             text="\nRETURN HOME\n",
                             font = "Arial 10",
                             bg = "#5b183a",
                             fg = "white",
                            activebackground="#b05b86",
                             command=lambda:show_frame(home_frame),
                             )
instruction_home.grid(row=1,
                      column=2,
                      columnspan=2,
                      pady=10,
                      padx=20
                      )

#---------------Home screen---------------
#Help icon
helpimage_path = "images/help.png"

helpphoto = tk.PhotoImage(file=helpimage_path)
helpimage_button = tk.Button(home_frame,
                     image=helpphoto,
                     bg="#5b183a",
                     activebackground = "#b05b86",
                     command=lambda:show_frame(help_frame))

helpimage_button.grid(row=0,
               column=2,
               columnspan=1)

#Home logo
homelogoimage_label = tk.Label(home_frame,
                               image=croplogophoto,
                               bg="#5b183a",)

homelogoimage_label.grid(row=0,
                         column=1,
                         pady=15
                         )

#Home image
homeimage_path = "images/home_img.png"

homephoto = tk.PhotoImage(file=homeimage_path)

homeimage_label = tk.Label(home_frame,
                           image=homephoto,
                           )

homeimage_label.grid(row=1,
                     column=1,
                     padx=0,
                     rowspan=3)#Stretches image through rows

#Successfully added order message
success_message = tk.StringVar()

success_label = tk.Label(home_frame,
                         textvariable=success_message,
                         fg="#21ff90",
                         bg = "#5b183a",
                         )

success_label.grid(row=5,
                   column=0,
                   pady=10)

#Welcome home message
home_message = tk.Label(home_frame,
                        text = "Welcome home!",
                        font = "Times 20 bold",
                        bg = "#5b183a",
                        fg = "white",
                        )
#Home options

order_option = tk.Button(home_frame,
                         text = "Order Menu",
                         command = lambda: [show_frame(order_frame),
                         success_message.set("")],
                         bg = "#5b183a",
                         fg = "white",
                         )

currentorder_option = tk.Button(home_frame,
                         text = "View Current orders",
                         bg = "#5b183a",
                         fg = "white",
                         command = lambda: [view_current_orders(),
                         success_message.set("")] #This message resets the success_message to "" so that the message disappears after entering a new frame)
                                )
gallery_option = tk.Button(home_frame,
                           text="View Menu Gallery",
                           bg = "#5b183a",
                           fg = "white",
                           command=lambda: [show_frame(menugallery_frame),
                           success_message.set("")])
#Main menu button
login_mmbutton=tk.Button(home_frame,
                         text="Main Menu",
                         bg = "#5b183a",
                         fg= "white",
                         command=lambda:show_frame(welcome_frame))

login_mmbutton.grid(row = 4,
                    column=0,
                    padx= 50,
                    pady = 8)
#Exit program button
home_exit=tk.Button(home_frame,
                       text="Exit program",
                       bg = "#5b183a",
                       fg = "white",
                       command=lambda:exit_program(),)
home_exit.grid(row = 4, column = 1, pady = 5, padx = 60,
                  )

#Home screen option grids
home_message.grid(row=0, column=0, padx= 50, pady = 8)
order_option.grid(row=1, column= 0, padx= 50, pady = 8)
currentorder_option.grid(row=2, column=0 , padx= 50, pady =8)
gallery_option.grid(row=3, column=0 , padx= 50, pady = 8)


#---------------Menu gallery screen---------------

#Gallery scrollbar
#scrollbar canvas
scroll_canvas = tk.Canvas(menugallery_frame,
                          width=500,
                          bg = "#5b183a",
                          )

scroll_canvas.pack(side="left",
                   fill="both",
                   expand=True,)

#Scrollbar syntax
scrollbar = ttk.Scrollbar(menugallery_frame,
                orient="vertical",
                command=scroll_canvas.yview,
                style="Gallery.Vertical.TScrollbar"

                ) #.yview moves the canvas when scrollbar is dragged)
#Place scrollbar on the right side
scrollbar.pack(side="right",
               fill="y",
               )

scroll_canvas.configure(yscrollcommand=scrollbar.set,)

#Frame to hold the scroll container
gallery_frame = tk.Frame(scroll_canvas,
                         bg = "#5b183a",
                         )
#Gallery frame link to scroll canvas
gallery_frame.bind(
    "<Configure>",
    #bbox("all") gets the size of everything inside canvas
    lambda e: scroll_canvas.configure(
        scrollregion=scroll_canvas.bbox("all"),
    )
)
#Scrollbar styling
style = ttk.Style()
style.theme_use("clam")  #allows more colour customisation

style.configure(
    "Gallery.Vertical.TScrollbar",
    bg="#5b183a",
    troughcolor="#5b183a",
    bordercolor="#5b183a",
)

#Put the gallery frame into the canvas
scroll_canvas.create_window((0,0),#(0,0) = top left corner
                            window=gallery_frame,
                            anchor="nw")#anchor="nw" means top-left alignment
#Gallery title
gallerytitle = tk.Label(gallery_frame,
                 text = "MENU GALLERY",
                 font = "Times 20 bold",
                 bg = "#5b183a",
                 fg = "white",)
gallerytitle.grid(row=0, column = 0, pady = 20, padx = 60)

#Logo
gallerylogo=tk.Label(gallery_frame,
         image=croplogophoto,
         bg="#5b183a")
gallerylogo.grid(row=0, column=2, padx=20,pady=20)

#Add image for each image in the food_images folder
for i, image_file in enumerate(os.listdir("food_images")):
    
    image_path = f"food_images/{image_file}"
    photo = tk.PhotoImage(file=image_path)
    
    #Add labels to each image
    item_name = image_file.replace(".png", "").replace("_", " ")
    item_label = tk.Label(gallery_frame,
                          text=item_name,
                          bg = "#5b183a",
                          fg = "white",
                          font = "Times 12 bold",)
    item_label.grid(row=i*2+1,
                    column=0,
                    padx=100,
                    pady=20,)
    image_label = tk.Label(gallery_frame,
                           image=photo)
    image_label.image = photo
    image_label.grid(row=i*2+2,
                     column=0)
#Home button
galleryhome_button = tk.Button(gallery_frame,
                    text="\nRETURN HOME\n",
                    command=lambda: show_frame(home_frame),
                    bg = "#5b183a",
                    fg = "white")

galleryhome_button.grid(row=1,
                column=2,
                padx=20,
                pady=0,
                )

#---------------Order screen---------------
#Logo
orderlogo=tk.Label(order_frame,
             image=croplogophoto,
             bg="#5b183a")
orderlogo.grid(row=0, column=1, padx=5,pady=5)
    
#order screen title
ordertitle = tk.Label(order_frame,
                 text = "ORDER MENU",
                 font = "Times 20 bold",
                 bg = "#5b183a",
                 fg = "white",)
ordertitle.grid(row=0, column = 0, pady = 15,
                padx=15)

#Spinboxes for option selection
#Generate a spinbox for each item
for i, (item, price) in enumerate(menu_prices):
    
    #Item labels
    item_label = tk.Label(order_frame,
                          text=item,
                          bg = "#5b183a",
                          fg = "white")
    item_label.grid(row = i+1, #the row increases for each item
                    column=0,
                    padx=20,
                    pady=5,
                    )
    #Price labels
    price_label = tk.Label(order_frame,
                           text=f"${price}",
                           bg = "#5b183a",
                           fg = "white")
    price_label.grid(row=i+1,
                     column=1,
                     padx=10,
                     pady=5,)

    #Generate spinboxes for menu items
    sb_var = tk.IntVar(value=0) #IntVar carries the value of the spinbox
    item_spinbox = tk.Spinbox(order_frame,
                              from_=0, to=100,
                              width=5,
                              textvariable=sb_var,
                              bg = "#5b183a",
                              fg = "#7c7e82")
    item_spinbox.grid(row=i+1,
                      column=2,
                      padx=20,
                      pady=5)
    
    ordered_items[item] = sb_var

#Button to confirm order
order_button = tk.Button(order_frame,
                        text = "Add to cart",
                        command = lambda:add_order(),
                        bg = "#5b183a",
                        fg = "white"
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
    #Open external order_number file to generate an order number
    with open("order_number.txt", "r") as file:
        order_number = int(file.read())
    #Write order invoice to an external file containing all information
    with open(f"{user_id}_order_{order_number}.txt", "x") as file:
        file.write(f"---BDSC CAFE ORDER {order_number}---\n")
        file.write(f"Student ID: {user_id}\n")
        file.write(f"-----------------------\n")
        file.write(f"Items Ordered:\n")
        for item in cart:
            file.write(f"- {item}\n")#This prints the items in the cart and the quantity
        file.write(f"STATUS: Processing\n")
        file.write(f"TOTAL: ${total_price}\n")
        file.write(f"-----------------------\n\n")
        
        order_number+=1
        with open("order_number.txt", "w") as file:
            file.write(str(order_number))
            cart.clear()
        #Make the success message on the home frame appear
        success_message.set("Order successfully added!")
                
        #Set spinbox value to 0
        for item, var in ordered_items.items():
            var.set(0)
    
    #After the ordering process has finished, the user returns to the home frame   
    show_frame(home_frame)
    
#Home button
orderhome_button = tk.Button(order_frame,
                    text="\nRETURN HOME\n",
                    command=lambda: show_frame(home_frame),
                    bg = "#5b183a",
                    fg = "white",)

orderhome_button.grid(row=2,
                column=3,
                padx=20,
                pady=0,)

    
#---------------Current order screen---------------
#Current order Scrollbar
#scrollbar canvas
orderscroll_canvas = tk.Canvas(currentorder_frame,
                            width=500,
                            bg = "#5b183a",
                               )
orderscroll_canvas.pack(side="left",
                    fill="both",
                    expand=True,
                        )

#Scrollbar syntax
orderscrollbar = ttk.Scrollbar(
    currentorder_frame,
    orient="vertical",
    command=orderscroll_canvas.yview, #.yview moves the canvas when scrollbar is dragged)
    style="CurrentOrders.Vertical.TScrollbar"
)

#Place scrollbar on the right side
orderscrollbar.pack(side="right",
                fill="y")

orderscroll_canvas.configure(yscrollcommand=orderscrollbar.set)

#Frame to hold the scroll container
current_frame = tk.Frame(orderscroll_canvas,
                         bg = "#5b183a",
                         )
#current frame link to scroll canvas
current_frame.bind(
    "<Configure>",
    #bbox("all") gets the size of everything inside canvas
    lambda e: orderscroll_canvas.configure(
        scrollregion=orderscroll_canvas.bbox("all")
    )
)

#Scrollbar styling for current orders
style = ttk.Style()
style.theme_use("clam")

style.configure(
    "CurrentOrders.Vertical.TScrollbar",
    bg="#5b183a",
    troughcolor="#5b183a",
    bordercolor="#5b183a",
)

#Put the gallery frame into the canvas
orderscroll_canvas.create_window((0,0),#(0,0) = top left corner
                            window=current_frame,
                            anchor="nw")#anchor="nw" means top-left alignment
#View Current orders function - runs each time current order screen opens
def view_current_orders():
    #Set row number to 0
    row_num = 1

    #Initially, no previous orders were found
    orders_found = False
    
    show_frame(currentorder_frame)

    #Clear old widgets INSIDE the scrolling frame
    for widget in current_frame.winfo_children():
        widget.destroy()
        
    #Refresh screen button
    #Refresh icon
    refreshimage_path = "images/refresh.png"
    refreshimage=tk.PhotoImage(file=refreshimage_path)
    refreshimage_button=tk.Button(current_frame,
                                image=refreshimage,
                                bg = "#5b183a",
                                command=lambda:view_current_orders(),
                                activebackground = "#b05b86")

    refreshimage_button.image = refreshimage
    refreshimage_button.grid(row=0,
                             column=3,
                             pady=7,
                             padx=4
                             )
        
    #current screen title
    currenttitle = tk.Label(current_frame,
                     text = "CURRENT ORDERS",
                     font = "Times 17 bold",
                     bg = "#5b183a",
                     fg = "white",)
    currenttitle.grid(row=0, column = 0, pady = 15,
                    padx=5)
    #Logo
    currentlogo=tk.Label(current_frame,
             image=croplogophoto,
             bg="#5b183a")
    currentlogo.grid(row=0, column=1, padx=5,pady=5)

    #Home button
    crntordhome_button = tk.Button(
        current_frame,
        text="\nRETURN HOME\n",
        command=lambda: show_frame(home_frame),
        bg = "#5b183a",
        fg = "white",
    )

    crntordhome_button.grid(row=0,
                            column=2,
                            padx=5,
                            pady=20)
    #Find current orders
    for file_name in os.listdir():
        if user_id in file_name:
            #Determine if an order invoice belonging to the user ID is found
            with open(file_name, "r") as file:
                current_order = file.read()
                orders_found = True

            #Order invoice label
            order_invoice = tk.Label(
                current_frame,
                text=current_order,
                bg = "#5b183a",
                fg = "white"
            )
            order_invoice.grid(row=row_num,
                               column=0,
                               padx=5,
                               pady=5)
            #Status setup
            status = ""
            
            #Change status colour depending on the status written in ext file
            if "Preparing" in current_order:
                status = "Preparing"
                colour = "orange"

            if "Ready" in current_order:
                status = "Pick up now!"
                colour = "#21ff90",
                
            elif "Processing" in current_order:
                status = "Processing"
                colour = "white",
                
            #Status label
            status_label = tk.Label(
                current_frame,
                text=status,
                fg=colour,
                bg = "#5b183a",
            )
            
            status_label.grid(row=row_num,
                              column=1,
                              padx=2,
                              pady=5)
            #Mark order as Completed button
            completed_button = tk.Button(
                current_frame,
                text="Mark as Completed",
                command=lambda file=file_name: remove_order(file), #Delete order once done
                bg = "#5b183a",
                fg = "white"
            )
            completed_button.grid(row=row_num,
                                  column=2,
                                  padx=5,
                                  pady=5)

            row_num += 1
    #Text to be displayed if no orders found
    if orders_found == False:

        no_orders_label = tk.Label(
            current_frame,
            text="No orders to display",
            bg = "#5b183a",
            fg = "white"
        )

        no_orders_label.grid(row=1,
                             column=0,
                             padx=5,
                             pady=5)

#Function to remove order from file
def remove_order(file):
    os.remove(file)
    view_current_orders()

# Show welcome screen first
show_frame(welcome_frame) 

# Run the program
root.mainloop()     
