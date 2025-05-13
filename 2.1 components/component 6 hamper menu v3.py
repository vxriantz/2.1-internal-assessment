"""This component displays the menu for a gift hamper establishment program"""

#list of premade hamper names
premade_hamper_names = ['Birthday Bliss', 'Get Well Soon', 'Luxury Gourmet', 'New Baby Hamper', 
               'Eco-Friendly Hamper', 'Home Sweet Home Hamper', 'A Little Thank You Basket']

#list of premade hamper prices
premade_hamper_prices = [49.99, 39.99, 89.99, 59.99, 44.99, 59.99, 49.99] 

#list of custom hamper names
custom_hamper_names = ['Chocolate Selection Box', 'Mini Wine Bottle', 'Cheese Wedges', 'Tea Sampler', 'Coffee Beans',
                       'Scented Candle', 'Bath Bomb', 'Face Mask', 'Essential Oil',
                       'Stuffed Toy', 'Handwritten Card', 'Gift Wrapping', 'Reusable Basket',
                       'Baby Booties', 'Teething Toy', 'Baby Shampoo', 'Soft Pacifier']

#list of custom hamper prices
custom_hamper_prices = [12.00, 15.00, 10.00, 8.00, 11.00,
                        9.00, 6.00, 5.00, 7.00,
                        10.00, 3.00, 5.00, 6.00, 
                        8.00, 6.00, 7.00, 5.00]


#displays the hamper menu
#counts through the premade and custom hamper names and prices and displays using a count
#prices formatted into currency
#count adjusted to start from 1
def hamper_menu():
    NUMBER_PREMADE_HAMPER = 7
    for count in range(NUMBER_PREMADE_HAMPER):
        print("{} {} ${:.2f}".format(count+1, premade_hamper_names[count], premade_hamper_prices[count])) 
    print() 
    NUMBER_CUSTOM_HAMPER = 17 
    for count in range(NUMBER_CUSTOM_HAMPER):
     print("{} {} ${:.2f}".format(count+1, custom_hamper_names[count], custom_hamper_prices[count]))


hamper_menu()