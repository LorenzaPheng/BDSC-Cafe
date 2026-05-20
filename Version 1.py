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

menu_prices = {
    "Chocolate milk" : "$3",
    "Sausage roll" : "$4",
    "Brownie" : "$2"}

#Empty list for users' ordered items
cart = []

#Initial menu - Logging in
def log_in():
    print("--------LOG IN--------")
    while True:
        entered_id = input("Enter student ID : ")
        if entered_id not in login_keys:
            print("ID not found")
        else:
            try:
                entered_pin = int(input("Enter PIN : "))
                for pin in login_keys:
                    if entered_pin == login_keys[pin]:
                        print("--------SUCCESSFULLY LOGGING IN--------\n")
                        main_menu()
                        break
                else:
                    print("PIN OR ID IS INCORRECT")
            except ValueError:
                print("Enter a valid PIN in integers")
log_in()       
def main_menu():
    print("--------MAIN MENU--------")
    print("OPTIONS:")
    print("1. Order Menu")
    print("2. Current orders")
    print("3. Exit")

    choice = int(input("Enter option (1/2/3) : "))
    if choice == 1:
        order_menu()
    if choice == 2:
        current_orders()
    if choice == 3:
        print("--------EXITING PROGRAM--------")
        sys.exit
