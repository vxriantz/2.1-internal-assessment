"""This component displays the customer's order details for a gift hamper establishment program"""

from colorama import Fore, Back, Style, init

#list to store ordered hampers
order_list = ['Birthday Bliss', 'Get Well Soon', 'Handwritten Card', 'Tea Sampler'] 
#list to store hamper prices
order_cost = [49.99, 39.99, 3.00, 8.00]  
#customer details 
customer_details = {'Name': 'Alex', 'Phone': '090800359', 'House': '45', 'Street': 'Harry', 'Suburb': 'Howick'}
init(autoreset=True)

def printorder():
    print()
    #print (Style.RESET_ALL)
    print(Fore.GREEN + "Customer Details")

    #print customer order 
    print(f"Customer Name: {customer_details['Name']}\nCustomer Phone: {customer_details['Phone']}\nCustomer Address: {customer_details['House']} {customer_details['Street']}, {customer_details['Suburb']}")
    print()
    print(Fore.GREEN + "Order Details")
    #print(Style.RESET_ALL)

    count = 0
    for item in order_list: 
        print(Style.BRIGHT + "Ordered: {} Cost: ${:.2f}".format(item, order_cost[count])) 
        count = count+1
    total_cost = sum(order_cost)
    print()
    print(Style.BRIGHT + "Total Cost: ${:.2f}".format(total_cost))
    print()

printorder()