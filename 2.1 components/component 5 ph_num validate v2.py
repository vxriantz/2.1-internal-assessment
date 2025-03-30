"""This component details collecting a customer's details for a jewelry establishment program"""

import re

#customer details dictionary
customer_details = {}

#regular expression pattern for phone validation 
pattern = r"^\d{8,10}$" 

#ask user for input
phone_number = input("Please enter your phone number: ")
if re.match(pattern,phone_number): 
    customer_details["phone"] = phone_number 
else: 
    print("This is an invalid phone number") 

print(customer_details) 