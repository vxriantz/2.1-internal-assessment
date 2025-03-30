"""This component details collecting a customer's details for a jewelry establishment program"""

import re 

#customer details dictionary
customer_details = {}

#while loop for validation of house number
while True: 
    question = "Please enter your house or apartment number: " 
    response = input(question) 
    if response == "":
        print("Cannot be left blank") 
    else:
        #removes blank spaces from response
        no_blanks = re.sub(r"\s+", "", response) 
        customer_details["house"] = response.title() 
        break 










print(customer_details)