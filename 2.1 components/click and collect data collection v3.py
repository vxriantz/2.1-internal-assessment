"""This component details collecting a customer's details for a pizza establishment program"""

import re

#customer details dictionary
customer_details = {}




def click_collect():
    #regular expression pattern for phone validation 
    pattern = r"^\d{8,10}$" 

    #while loop for validation of name
    while True: 
        question = "Please enter your name: " 
        response = input(question) 
        #removes blank spaces from response
        no_blanks = re.sub(r"\s+", "", response) 
        #checking if input is alphabetical
        x = no_blanks.isalpha() 
        if x == False: 
            #if not then print error message
            print("Input must only contain letters") 
        else: 
            #if alpha convert to title case and append to dictionary
            customer_details["name"] = response.title() 
            break 


    #while loop for validation of phone number 
    while True:
        #ask user for input
        question = ("Please enter your phone number: ")
        response = input(question) 
        #removes blank spaces from response
        no_blanks = re.sub(r"\s+", "", response) 
        if re.match(pattern,no_blanks): 
            phone_number = no_blanks
            customer_details["phone"] = phone_number 
            break
        else: 
            print("This is an invalid phone number") 

click_collect()

print(customer_details) 