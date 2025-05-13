"""This component will display a section for the user to make a new order or cancel their order for a gift hamper establishment program""" 

#constant variables for low and high number for menus
LOW = 1
HIGH = 2 

#function validates integers
#takes parameters of low and high numbers and question
#input must be integer between low and high parameters
#while loop until correct input is received then returns input to original function
#value error results in error message and new input request
def integer_validation(low, high, question): 
       while True:
         try:
            num = int(input(question))
            if num >= low and num <= high:
                return num
            else: 
                (f"Please enter {LOW} or {HIGH} ")
         except ValueError:
            print("That is not a valid number") 
            (f"Please enter {LOW} or {HIGH} ")


#function allowing users to choose to either make a new order or cancel their order
#input request sent to integer_validation function for validation
#valid input is returned and sent to if statements for appropriate action
def new_exit(): 
    del_pick = ""
    print("Do you want to start a new order or exit program?") 
    question = (f"Please enter {LOW} or {HIGH} ")
    print("Enter 1 to for new order")
    print("Enter 2 to exit") 
    del_pick = integer_validation(LOW, HIGH, question)
    if del_pick == 1:
        print("New Order") 
    elif del_pick == 2:
        print("Exit")


new_exit()