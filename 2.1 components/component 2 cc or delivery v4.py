"""This component will detail the options for delivery for a pizza establishment program"""
LOW = 1
HIGH = 2 
print("Do you want click and collect or delivery?") 
print("Enter 1 for click and collect")
print("Enter 2 for delivery") 

while True:
    try:
        num = int(input("Please enter 1 or 2 ")) 
        if num >= LOW and num <= HIGH: 
            if num == 1:
                print("click and collect") 
                break
            elif num == 2:
                print("delivery")
                break
            else: num = int(input("Invalid number. Please enter 1 or 2 "))

    except ValueError:
        print("That is not a valid number, please only enter 1 or 2") 

print("Continue") 
