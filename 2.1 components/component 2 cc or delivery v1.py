"""This component will detail the options for delivery for a gift hamper establishment program"""

print("Do you want click and collect or delivery?") 
print("Enter 1 for click and collect")
print("Enter 2 for delivery") 
choice = int(input("Please enter 1 or 2")) 
if choice == 1:
    print("click and collect") 
elif choice == 2:
    print("delivery")
else: print("Error") 