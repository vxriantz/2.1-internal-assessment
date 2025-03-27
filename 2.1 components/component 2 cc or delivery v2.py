"""This component will detail the options for delivery for a gift box establishment program"""
print("Do you want click and collect or delivery?") 
print("Enter 1 for click and collect")
print("Enter 2 for delivery") 

try:
    choice = int(input("Please enter 1 or 2")) 
except ValueError:
    print("That is not a valid number") 

if choice == 1:
    print("click and collect") 
elif choice == 2:
    print("delivery")
else: print("Error") 
