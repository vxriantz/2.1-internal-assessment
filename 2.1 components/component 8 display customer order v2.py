#list to store ordered hampers
order_list = ['Birthday Bliss', 'Get Well Soon', 'Handwritten Card', 'Tea Sampler'] 
#list to store hamper prices
order_cost = [49.99, 39.99, 3.00, 8.00] 

#customer details 
customer_details = {'Name': 'Alex', 'Phone': '090800359', 'House': '45', 'Street': 'Harry', 'Suburb': 'Howick'}

#print customer order 
print(f"Customer Name: {customer_details['Name']}\nCustomer Phone: {customer_details['Phone']}\nCustomer Address: {customer_details['House']} {customer_details['Street']}, {customer_details['Suburb']}")

count = 0
for item in order_list: 
    print("Ordered: {} Cost: ${:.2f}".format(item, order_cost[count])) 
    count = count+1