"""This component details collecting a customer's details for a gift hamper establishment program"""

import re 

#customer details dictionary
customer_details = {}



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


print(customer_details)

