#list to store ordered hampers
order_list = ['Birthday Bliss', 'Get Well Soon', 'Handwritten Card', 'Tea Sampler'] 
#list to store hamper prices
order_cost = [49.99, 39.99, 3.00, 8.00] 


count = 0
for item in order_list: 
    print("Ordered: {} Cost: ${:.2f}".format(item, order_cost[count])) 
    count = count+1