"""This program will display a BOT that takes customer's orders for a gift hamper establishment"""
# Pizza BOT
# Programmer Alexander Goddard
# Achievement Standard AS91896 & AS91897
# Known Bugs - None 

# import libraries to support extended functionality
import random #used to select random BOT names
import re #used for regular expressions in input validation

# import pandas library
import pandas as pd #used to display product menus in a structured table format

# import system
# enables program to use exit()
import sys

# import random integer
from random import randint #used to generate random numbers for BOT names

# import colorama 
from colorama import Fore, Back, Style, init # allows program to create coloured text

# list of names used by BOT
bot_names = ["Anthony", "Clint", "Gamora", "Howard", "Wanda", "Clara", "James", "Steve", "Natasha", "Sam"]

# list of hamper names
hamper_names = ['Birthday Bliss', 'Get Well Soon', 'Luxury Gourmet', 'New Baby Hamper', 
                                   'Eco-Friendly Hamper', 'Home Sweet Home Hamper', 'A Little Thank You Basket', 
                                   'Chocolate Selection Box', 'Mini Wine Bottle', 'Cheese Wedges', 'Tea Sampler', 'Coffee Beans',
                                   'Scented Candle', 'Bath Bomb', 'Face Mask', 'Essential Oil',
                                   'Stuffed Toy', 'Handwritten Card', 'Gift Wrapping', 'Reusable Basket',
                                   'Baby Booties', 'Teething Toy', 'Baby Shampoo', 'Soft Pacifier']

# list of hamper prices
hamper_prices = [49.99, 39.99, 89.99, 59.99, 44.99, 59.99, 49.99, 
                 12.00, 15.00, 10.00, 8.00, 11.00,
                 9.00, 6.00, 5.00, 7.00,
                 10.00, 3.00, 5.00, 6.00, 
                 8.00, 6.00, 7.00, 5.00] 

# customer details dictionary
customer_details = {}

# list to store ordered hampers
order_list = [] 
# list to store hamper prices
order_cost = [] 

# constant variables for low and high number for menus
LOW = 1
HIGH = 2 
#set autoreset to true so that coloured text automatically stops at end of print statement
init(autoreset=True)


# function validates integers
# takes parameters of low and high numbers and question
# input must be integer between low and high parameters
# while loop until correct input is received then returns input to original function
# value error results in error message and new input request
def integer_validation(low, high, question): 
       while True: #sets up while loop
         try:
            num = int(input(question)) #asks for integer input
            if num >= low and num <= high:
                return num #if number is above or below the low (1) and high (2) values, return back to num
            else: 
                (f"Please enter {LOW} or {HIGH} ") #asks user to enter the low (1) or high (2) values
         except ValueError:
            print()
            print(Fore.RED + "That is not a valid number") #if input is not int, prints error message
            print()
            (f"Please enter {LOW} or {HIGH} ") #asks question again


# function validates string
# removes blank spaces before checking
# input must be string
# while loop until correct input is received then returns input to original function 
# value error results in error message and new input request
def validate_alpha(question): 
    # while loop for validation of street name
    while True: #sets up while loop
        response = input(question) #asks for string input to 'question' variable
        # remove any spaces or blanks
        no_blanks = re.sub(r"\s+", "", response) 
        # checking if input is alphabetical
        x = no_blanks.isalpha()
        if x == False: #if x is false then print error message
            print()
            print(Fore.RED + "Input must only contain letters")
            print()
        else: 
            # if alpha convert to title case and append to dictionary
            return response


# function creates welcome message and generates random name for BOT
def welcome():
    num = randint(0,9) #chooses a random name from list of BOT names
    name = (bot_names[num]) #puts randomly chosen name into a variable
    print("*** Welcome to The Giftery ***")
    print("*** My name is", name,"***") #prints statement using the variable
    print("*** I will be here to help you order your perfect gift hamper! ***")


# function allowing users to choose either click and collect or delivery
# input request sent to integer_validation function for validation
# valid input is returned and sent to if statements for appropriate action
def pickup_delivery(): 
    del_pick = ""
    print()
    print(Style.BRIGHT + "Do you want click and collect or delivery?") 
    question = (f"Please enter {LOW} or {HIGH} ")
    print()
    print("Enter 1 for click and collect")
    print("Enter 2 for delivery") 
    print()
    del_pick = integer_validation(LOW, HIGH, question)
    if del_pick == 1: #if input is 1, continue to click_collect function
        click_collect()
    elif del_pick == 2: #if input is 2, continue to click_collect and delivery_info functions
        click_collect()
        delivery_info()
    return del_pick


# collect click and collect data function
    # function collects customer data for click and collect
    # phone number validated using regular expression pattern
    # string validated using isalpha
    # while loop until correct input is received then returns input to original function 
def click_collect():
    # regular expression pattern for phone validation (8 to 10 digits)
    pattern = r"^\d{8,10}$" 

    print()

    # while loop for validation of name
    while True: #sets up while loop
        question = "Please enter your name: " 
        response = input(question) #asks for input to question variable
        # removes blank spaces from response
        no_blanks = re.sub(r"\s+", "", response) 
        # checking if input is alphabetical
        x = no_blanks.isalpha() 
        if x == False: # if x is false then print error message
            print()
            print(Fore.RED + "Input must only contain letters")
            print()
        else: 
            # if alpha convert to title case and append to dictionary
            customer_details["Name"] = response.title() 
            break 

    print()     

    # while loop for validation of phone number 
    while True: #sets up while loop
        # ask user for input
        question = ("Please enter your phone number: ")
        response = input(question) 
        # removes blank spaces from response
        no_blanks = re.sub(r"\s+", "", response) 
        if re.match(pattern,no_blanks): 
            phone_number = no_blanks
            customer_details["Phone"] = phone_number #append to dictionary
            break
        else: #if input is not valid then print error message
            print()
            print(Fore.RED + "This is an invalid phone number") 
            print()


# collect delivery data 
    # function collects customer data for delivery
    # house number validated using regular expression pattern
    # string validated using isalpha
    # while loop until correct input is received then returns input to original function    
def delivery_info():
    # while loop for validation of house number
    while True: #sets up while loop
        print()
        question = "Please enter your house or apartment number: " 
        response = input(question) #asks for input to 'question' variable
        if response == "": #if input is blank, print error message
            print()
            print(Fore.RED + "Cannot be left blank") 
            print()
        else:
            no_blanks = re.sub(r"\s+", "", response) #removes blank spaces from response
            customer_details["House"] = response.title() #converts to title case and appends to dictionary
            break 

    print()

    # while loop for validation of street name
    question = "Please enter your street name: " 
    response = validate_alpha(question) 
    # if alpha convert to title case and append to dictionary
    customer_details["Street"] = response.title() 

    print()

    # while loop for validation of suburb
    question = "Please enter your suburb name: " 
    response = validate_alpha(question) 
    # if alpha convert to title case and append to dictionary
    customer_details["Suburb"] = response.title() 


# hamper menu display
# uses the pandas library to display the hamper menu
# create premade_hamper_menu function
def premade_hamper_menu():
    # create menu dictionary
    menu_dict = {}

    # format hamper prices as currency
    pd.options.display.float_format = '${:,.2f}'.format 

    # add premade hamper numbers to dictionary
    menu_dict ['Number'] = [1,2,3,4,5,6,7]

    # add premade hamper names to dictionary
    menu_dict ['Premade Hampers'] = ['Birthday Bliss', 'Get Well Soon', 'Luxury Gourmet', 'New Baby Hamper', 
               'Eco-Friendly Hamper', 'Home Sweet Home Hamper', 'A Little Thank You Basket']

    # add premade hamper blank column to dictionary
    menu_dict [""] = ["","","","","","",""]

    # add premade hamper prices to dictionary 
    menu_dict ['Price'] = [49.99, 39.99, 89.99, 59.99, 44.99, 59.99, 49.99] 

    # display menu dataframe
    df = pd.DataFrame(menu_dict) 
    blankIndex = [''] * len(df) 
    df.index = blankIndex 

    print()
    print(Fore.GREEN + "Premade Hamper Menu: Please order using the menu item's number \n \n",df) 


# create custom_hamper_menu function
def custom_hamper_menu():
    # create menu dictionary
    menu_dict = {}

    # format hamper prices as currency
    pd.options.display.float_format = '${:,.2f}'.format 

    # add custom hamper numbers to dictionary
    menu_dict ['Number'] = [8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

    # add custom hamper item names to dictionary
    menu_dict ['Custom Hamper Items'] = ['Chocolate Selection Box', 'Mini Wine Bottle', 'Cheese Wedges', 'Tea Sampler', 'Coffee Beans',
                                    'Scented Candle', 'Bath Bomb', 'Face Mask', 'Essential Oil',
                                    'Stuffed Toy', 'Handwritten Card', 'Gift Wrapping', 'Reusable Basket',
                                    'Baby Booties', 'Teething Toy', 'Baby Shampoo', 'Soft Pacifier']

    # add custom hamper blank column to dictionary
    menu_dict [""] = ["","","","","","","","","","","","","","","","",""]

    # add custom hamper prices to dictionary 
    menu_dict ['Price'] = [12.00, 15.00, 10.00, 8.00, 11.00,
                        9.00, 6.00, 5.00, 7.00,
                        10.00, 3.00, 5.00, 6.00, 
                        8.00, 6.00, 7.00, 5.00] 
    
    # display menu dataframe
    df = pd.DataFrame(menu_dict) 
    blankIndex = [''] * len(df) 
    df.index = blankIndex 

    print()
    print(Fore.GREEN + "Custom Hamper Menu: Please order using the menu item's number \n \n",df) 
    print()


# customer hamper order 
    # function stores hamper order data 
    # while loop until correct input is received then returns input to original function
def hamper_order():
    num_hampers = 0
    while True: #sets up while loop
        try:
            num_hampers = int(input("How many hampers do you want to order? ")) #asks user for int input 
            if num_hampers >=1 and num_hampers <= 5: #adds boundaries to input request
                break
            else:
                print()
                print(Fore.RED + "Your order must be between 1 and 5 hampers") #if input is out of given boundaries, prints error message
                print()
        except ValueError:
            print() 
            print(Fore.RED + "This is not a valid number") #if input is not valid, prints error message
            print()

    print(num_hampers)
    print()

    #choose hampers from the menu
    print("Please choose hamper(s) from the menu") 
    print()
    for item in range(num_hampers): 
        while num_hampers > 0: #sets up while loop
            while True:
                try:
                    hampers_ordered = int(input()) #asks user for int input
                    if hampers_ordered >=1 and hampers_ordered <= 24: #add boundaries to input request
                        break
                    else: #if input is out of given boundaries, prints error message
                        print(Fore.RED + "Your hamper order must be between 1 and 24")
                        print()
                except ValueError: #if input is not valid, prints error message
                    print(Fore.RED + "That is not a valid number")
                    print()

            hampers_ordered = hampers_ordered-1 #adjusts user's input to match python's zero-based indexing
            order_list.append(hamper_names[hampers_ordered]) #adds name of selected hampers to the order list
            order_cost.append(hamper_prices[hampers_ordered]) #add price of selected hampers to the order list
            print("{} ${:.2f}".format(hamper_names[hampers_ordered], hamper_prices[hampers_ordered])) #prints name and price of selected hampers and formats to 2dp
            num_hampers = num_hampers-1 #decreases the number of hampers the user still needs to order when ordering

    print(order_list)
    print(order_cost)


# function displays customer order
    # prints customer order
    # accounting for differences with click and cllect or delivery data
    # takes del-pick as parameter
    # returns nothing
def print_order(del_pick):
    print()
    # print customer order
    print(Fore.GREEN + "Customer Details")
    # to account for different data collected for click and collect and delivery
    if del_pick ==1: #if input is 1, print below stored information
        print("Collection Method: Click and Collect")
        print(f"Customer Name: {customer_details['Name']}\nCustomer Phone: {customer_details['Phone']}")
    else: #if input is 2, print below stored information
     print("Collection Method: Delivery")
     print(f"Customer Name: {customer_details['Name']}\nCustomer Phone: {customer_details['Phone']}\nCustomer Address: {customer_details['House']} {customer_details['Street']}, {customer_details['Suburb']}")
     
    print()
    print(Fore.GREEN + "Order Details")

    count = 0
    for item in order_list: #formats ordered items to bold, displays ordered items and cost of each item
        print(Style.BRIGHT + "Ordered: {} Cost: ${:.2f}".format(item, order_cost[count])) 
        count = count+1
        print()
    #calculate the total cost of the order using sum
    total_cost = sum(order_cost)
    #calculate delivery fee
    delivery_fee = 0
    if total_cost < 50: 
        delivery_fee = 14
        print() 
        print(Fore.YELLOW + "Orders under $50 have a $14 delivery fee.")
    
    total_cost = total_cost + delivery_fee
    print()
    print(Style.BRIGHT + Fore.GREEN + f"Your total cost including the delivery is: ${total_cost:.2f}")
    print() 


# confirm or cancel order 
    # uses integer_validation function to validate input
def continue_cancel(): 
    del_pick = ""
    print("Do you want to continue with the order?") 
    print()
    question = (f"Please enter {LOW} or {HIGH} ")
    print("Enter 1 to continue")
    print("Enter 2 to cancel") 
    print()
    del_pick = integer_validation(LOW, HIGH, question)
    if del_pick == 1: #if input is 1, print thank you messages in green
        print()
        print(Fore.GREEN + "Thank you for your order!") 
        print()
        print(Fore.GREEN + "Your order has been sent to the manufacturers.") 
        print()
        print(Fore.GREEN + "You will receive a text when it is ready to pickup or out for delivery.")
        print()
    elif del_pick == 2: #if input is 2, print cancel message in red
        print()
        print(Fore.RED + "Your order has been cancelled.")
        print()


# exit program or start a new order
    # uses integer_validation function to validate input
def new_exit(): 
    del_pick = ""
    print("Do you want to start a new order or exit program?") 
    print()
    question = (f"Please enter {LOW} or {HIGH} ")
    print("Enter 1 to for new order")
    print("Enter 2 to exit") 
    print()
    del_pick = integer_validation(LOW, HIGH, question)
    if del_pick == 1: #if input is 1, clear data from lists, and rerun main function
        print()
        print(Fore.GREEN + "New Order") 
        print()
        # clear data from lists
        order_list.clear()
        order_cost.clear()
        # run main function
        main()
    elif del_pick == 2: #if input is 2, print thank you message, clear data from lists, and exit program
        print()
        print(Fore.GREEN + "Thank you for visiting the Giftery!")
        print()
        # clear data from lists
        order_list.clear()
        order_cost.clear()
        # exit program
        exit()

# create main function
def main():
    welcome()
    del_pick = pickup_delivery()
    premade_hamper_menu()
    custom_hamper_menu()
    hamper_order()
    print_order(del_pick)
    continue_cancel()
    new_exit()

# runs all component functions in order
main() 

# prints receipt of user's input details
print(customer_details)