"""This component displays the menu for a gift hamper establishment program"""

#list of pizza names
pizza_names = ['Margherita', 'Pepperoni', 'Hawaiian', 'Cheese', 'Italian', 'Veggie', 'Vegan', 'Chicken Deluxe',
               'Mega Meat Lovers', 'Seafood Deluxe', 'Apricot Chicken Deluxe', 'BBQ Chicken Deluxe']
#list of pizza prices
pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50] 



#displays the pizza menu
#counts through the pizza names and prices and displays using a count
#prices formatted into currency
#count adjusted to start from 1
def pizza_menu():
    NUMBER_PIZZA = 12
    for count in range(NUMBER_PIZZA):
        print("{} {} ${:.2f}".format(count+1, pizza_names[count], pizza_prices[count])) 



pizza_menu()