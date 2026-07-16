'''BDSC cafe program'''
'''This is a click and collect program that signs users' in using their
student ID, collects their orders and allows them to mark their order as completed'''
#
import sys, os 

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
