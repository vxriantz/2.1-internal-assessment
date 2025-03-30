"""This component details collecting a customer's details for a jewelry establishment program"""

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
        phone_number = response
        if re.match(pattern,response): 
            customer_details["phone"] = response 
            break
        else: 
            print("This is an invalid phone number") 

print(customer_details) 

click_collect()