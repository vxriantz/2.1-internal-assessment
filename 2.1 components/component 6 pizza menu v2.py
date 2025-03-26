"""This component displays the menu for a pizza establishment program"""

pizza_names = ['Margherita', 'Pepperoni', 'Hawaiian', 'Cheese', 'Italian', 'Veggie', 'Vegan', 'Chicken Deluxe',
               'Mega Meat Lovers', 'Seafood Deluxe', 'Apricot Chicken Deluxe', 'BBQ Chicken Deluxe']

pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50] 


NUMBER_PIZZA = 12

for count in range(NUMBER_PIZZA):
    print("{} {} ${:.2f}".format(count+1, pizza_names[count], pizza_prices[count])) 