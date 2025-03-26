"""This component details collecting a customer's details for a pizza establishment program"""

import re 

#customer details dictionary
customer_details = {}


def validate_alpha(question): 
    #while loop for validation of street anme
    while True:
        response = input(question) 
        #remove any spaces or blanks
        no_blanks = re.sub(r"\s+", "", response)
        #checking if input is alphabetical
        x = no_blanks.isalpha()
        if x == False: 
            #if not then print error message
            print("Input must only contain letters")
        else: 
            #if alpha convert to title case and append to dictionary
            return response


def delivery_info():
    #while loop for validation of street name
    question = "Please enter your street name: " 
    response = validate_alpha(question) 
    #if alpha convert to title case and append to dictionary
    customer_details["street"] = response.title() 

    #while loop for validation of suburb
    question = "Please enter your suburb name: " 
    response = validate_alpha(question) 
    #if alpha convert to title case and append to dictionary
    customer_details["suburb"] = response.title() 


delivery_info()


print(customer_details)