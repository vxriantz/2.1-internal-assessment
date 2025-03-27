"""This component displays the menu for a gift box establishment program"""

#import pandas library
import pandas as pd

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