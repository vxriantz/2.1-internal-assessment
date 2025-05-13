# Gift Hamper Shop - Sample Code 
# AS91896 + AS91897 Level 2 Project

# imports
from colorama import Fore, Back, Style, init

# Pre-made hamper item list
pre_made_hampers = [
    {
        "name": "Birthday Bliss", 
        "items": ["Mini Cake", "Birthday Card", "Balloon", "Scented Candle", "Chocolate Bar"], 
        "price": 49.99 
    }, 
    {
        "name": "Get Well Soon", 
        "items": ["Herbal Tea", "Puzzle Book", "Warm Socks", "Honey Jar", "Soft Toy"], 
        "price": 39.99
    }, 
    {
        "name": "Luxury Gourmet", 
        "items": ["Red Wine", "Brie Cheese", "Artisan Crackers", "Truffle Oil", "Premium Chocolate"], 
        "price": 89.99
    }, 
    {
        "name": "New Baby Hamper", 
        "items": ["Baby Blanket", "Teething Ring", "Onesie", "Baby Lotion", "Soft Rattle"], 
        "price": 59.99
    }, 
    {
        "name": "Eco-Friendly Hamper", 
        "items": ["Bamboo Cutlery", "Reusable Coffee Cup", "Organic Soap", "Plant Seeds", "Eco Tote"], 
        "price": 44.99
    }
]

# Custom hamper items with prices
custom_items = {
    "Chocolate Selection Box": 12.00,
    "Mini Wine Bottle": 15.00,
    "Cheese Wedges": 10.00,
    "Tea Sampler": 8.00, 
    "Coffee Beans": 11.00,
    "Scented Candle": 9.00, 
    "Bath Bomb": 6.00, 
    "Face Mask": 5.00, 
    "Essential Oil": 7.00, 
    "Stuffed Toy": 10.00, 
    "Handwritten Card": 3.00, 
    "Gift Wrapping": 5.00, 
    "Reusable Basket": 6.00,
    "Baby Booties": 8.00, 
    "Teething Toy": 6.00, 
    "Baby Shampoo": 7.00
}

# Cart
cart = [] 

# main menu function
def display_main_menu(): 
    print("\n==== Welcome to The Giftery ====")
    print("1. View Pre-Made Hampers") 
    print("2. Create a Custom Hamper")
    print("3. View Cart") 
    print("4. Checkout") 
    print("5. Exit") 

# pre made hamper function
def view_pre_made_hampers(): 
    print("\n--- Pre-Made Hampers ---") 
    for i, hamper in enumerate(pre_made_hampers): 
        print(f"{i + 1}. {hamper['name']} - ${hamper['price']}")
    print("")
    choice = input("Enter the number to add the corresponding hamper to your cart or press 'Enter' to return: ") 
    if choice.isdigit() and 1 <- int(choice) <= len(pre_made_hampers): 
        cart.append(pre_made_hampers[int(choice) - 1])
        print(Fore.GREEN + "Hamper added to cart.")
        print(Style.RESET_ALL)
    else: 
            print("")
            print(Fore.RED + "Invalid option.") 
            print(Style.RESET_ALL)
     
# custom hamper function
def create_custom_hamper():
    print("\n--- Create Your Custom Hamper ---") 
    custom_hamper = {
        "name": "Custom Hamper",
        "items": [],
        "price": 0.00
    }
    while True:
        print("\nAvailable Items:")
        for i, (item, price) in enumerate(custom_items.items(), 1): 
            print(f"{i}. {item} - ${price}") 
        print("")
        print("0. Finish and add to cart or return to menu") 
        print("")
        choice = input("Select an item number to add: ")
        if choice == "0": 
            break 
        elif choice.isdigit() and 1 <= int(choice) <= len(custom_items): 
            item_name = list(custom_items.keys())[int(choice) - 1]
            item_price = custom_items[item_name] 
            custom_hamper["itmes"].append(item_name)
            custom_hamper["price"] += item_price 
            print(f"Added {item_name}")
        else: 
            print(Fore.RED + "Invalid option.") 
            print(Style.RESET_ALL)
    if custom_hamper["items"]: 
        cart.append(custom_hamper) 
        print(Fore.GREEN + "Custom Hamper Added to cart.") 
        print(Style.RESET_ALL)

# view shopping cart function
def view_cart(): 
    if not cart: 
        print(Fore.RED + "\n Your cart is empty.") 
        print(Style.RESET_ALL)
        return 
    print("\n--- Your Cart ---") 
    total = 0
    for i, hamper in enumerate(cart, 1): 
        print(f"{i}. {hamper['name']} - ${hamper['price']:.2f}")
        print(f"    Items: {', '.join(hamper['items'])}")
        total += hamper['price'] 
    print(f"Total: ${total:.2f}") 

# check out function (finalise purchase)
def checkout(): 
    if not cart: 
        print(Fore.RED + "\nYour cart is empty. Add hampers before checking out.") 
        print(Style.RESET_ALL)
        return 
    view_cart()
    confirm = input("Would you like to confirm your order? (y/n): ").lower() 
    if confirm == "y": 
        print(Fore.GREEN + "Thank you for your purchase") 
        print(Style.RESET_ALL)
        cart.clear() 
    else: 
        print(Fore.RED + "Order not confirmed.") 
        print(Style.RESET_ALL)

# Main LOOP 
while True: 
    display_main_menu() 
    choice = input("Enter your choice (1-5): ") 
    if choice == "1": 
        view_pre_made_hampers() 
    elif choice == "2":
        create_custom_hamper() 
    elif choice == "3": 
        view_cart() 
    elif choice == "4": 
        checkout() 
    elif choice == "5": 
        print("")
        print(Fore.GREEN + "Thank you for visiting the Giftery. Goodbye!") 
        break 
    else: 
        print("")
        print(Fore.RED + "Invalid selection, please try again.")
        print(Style.RESET_ALL)