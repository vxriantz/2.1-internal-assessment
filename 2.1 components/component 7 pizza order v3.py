"""This component displays the menu for a gift box establishment program"""

#import pandas library
import pandas as pd

#list of pizza names
pizza_names = ['Margherita', 'Pepperoni', 'Hawaiian', 'Cheese', 'Italian', 'Veggie', 'Vegan', 'Chicken Deluxe',
               'Mega Meat Lovers', 'Seafood Deluxe', 'Apricot Chicken Deluxe', 'BBQ Chicken Deluxe']
#list of pizza prices
pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50] 

#list to store ordered pizzas
order_list = [] 
#list to store pizza prices
order_cost = [] 


#create pizza_menu function
def pizza_menu():
    #create menu dictionary
    menu_dict = {}

    #format pizza prices as currency
    pd.options.display.float_format = '${:,.2f}'.format 

    #add pizza numbers to dictionary
    menu_dict ['Number'] = [1,2,3,4,5,6,7,8,9,10,11,12]

    #add pizza names to dictionary
    menu_dict ['Pizzas'] = ['Margherita', 'Pepperoni', 'Hawaiian', 'Cheese', 'Italian', 'Veggie', 'Vegan', 'Chicken Deluxe',
                'Mega Meat Lovers', 'Seafood Deluxe', 'Apricot Chicken Deluxe', 'BBQ Chicken Deluxe']

    #add pizza blank column to dictionary
    menu_dict [""] = ["","","","","","","","","","","","",]

    #add pizza prices to dictionary 
    menu_dict ['Price'] = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50] 

    #display menu dataframe
    df = pd.DataFrame(menu_dict) 
    blankIndex = [''] * len(df) 
    df.index = blankIndex 

    print()
    print("Pizza Menu: Please order using the menu item's number \n \n",df) 
    print()

pizza_menu()

def pizza_order():
    num_pizzas = 0
    while True: 
        try:
            num_pizzas = int(input("How many pizzas do you want to order? "))
            if num_pizzas >=1 and num_pizzas <= 5:
                break
            else:
                print("Your order must be between 1 and 5 pizzas")
        
        except ValueError: 
            print("This is not a valid number")

    print(num_pizzas)

    #choose pizzas from the menu
    print("Please choose pizza from the menu") 
    for item in range(num_pizzas): 
        while num_pizzas > 0: 
            while True:
                try:
                    pizza_ordered = int(input()) 
                    if pizza_ordered >=1 and pizza_ordered <= 12:
                        break
                    else:
                        print("Your pizza order must be between 1 and 12")
                except ValueError: 
                    print("That is not a valid number")

            pizza_ordered = pizza_ordered-1
            order_list.append(pizza_names[pizza_ordered]) 
            order_cost.append(pizza_prices[pizza_ordered]) 
            print("{} ${:.2f}".format(pizza_names[pizza_ordered], pizza_prices[pizza_ordered]))
            num_pizzas = num_pizzas-1

    print(order_list)
    print(order_cost)

pizza_order()