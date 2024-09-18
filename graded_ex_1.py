# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_categories():
    print("Available Categories:")
    category_list = list(products.keys())
    for idx, category in enumerate(category_list, start=1):
        print(f"{idx}. {category}")
    
    category_choice = input("Select a category by number: ")
    
    if category_choice.isdigit():
        category_index = int(category_choice) - 1
        if 0 <= category_index < len(category_list):
            return category_index
    return None

def display_products(products_list):
    for idx, (product, price) in enumerate(products_list, start=1):
        print(f"{idx}. {product} - ${price:.2f}")

def display_sorted_products(products_list, sort_order):
    sorted_products = sorted(products_list, key=lambda x: x[1], reverse=(sort_order == "desc"))
    display_products(sorted_products)
    return sorted_products

def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity)) 

def display_cart(cart):
    print("\nYour Shopping Cart:")
    total_cost = 0
    for item in cart:
        total_price = item[1] * item[2]
        print(f"{item[0]} - ${item[1]:.0f} x {item[2]} = ${total_price:.0f}")
        total_cost += total_price
    print(f"Total cost: ${total_cost:.0f}")
    return total_cost

def generate_receipt(name, email, cart, total_cost, address):
    print("\n--- Receipt ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print("Items Purchased:")
    for item in cart:
        total_price = item[1] * item[2]
        print(f"{item[0]} - ${item[1]:.0f} x {item[2]} = ${total_price:.0f}")
    print(f"Total Cost: ${total_cost:.0f}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")

def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

def validate_email(email):
    return "@" in email

def main():
    cart = []

    # Get user details
    name = input("Enter your full name (First Last): ")
    while not validate_name(name):
        print("Invalid name. Please enter a valid name (First Last).")
        name = input("Enter your full name (First Last): ")

    email = input("Enter your email address: ")
    while not validate_email(email):
        print("Invalid email. Please enter a valid email address.")
        email = input("Enter your email address: ")

    # Show categories
    category_index = display_categories()
    if category_index is None:
        print("Invalid category selected.")
        return

    category_list = list(products.keys())
    selected_category = category_list[category_index]
    selected_products = products[selected_category]

    while True:
        # Display products
        display_products(selected_products)
        
        print("\nOptions:")
        print("1. Select a product to buy")
        print("2. Sort products by price")
        print("3. Go back to category selection")
        print("4. Finish shopping")

        option = int(input("Select an option: "))
        
        if option == 1:
            product_choice = int(input("Enter the product number you want to buy: ")) - 1
            if 0 <= product_choice < len(selected_products):
                quantity = int(input("Enter the quantity you want to buy: "))
                add_to_cart(cart, selected_products[product_choice], quantity)
            else:
                print("Invalid product number.")

        elif option == 2:
            sort_order = input("Sort by price: asc or desc: ")
            while sort_order not in ["asc", "desc"]:
                print("Invalid choice. Please select 'asc' or 'desc'.")
                sort_order = input("Sort by price: asc or desc: ")
            display_sorted_products(selected_products, sort_order)

        elif option == 3:
            category_index = display_categories()
            if category_index is None:
                print("Invalid category selected.")
                return
            selected_category = category_list[category_index]
            selected_products = products[selected_category]

        elif option == 4:
            if cart:
                total_cost = display_cart(cart)
                address = input("Enter your delivery address: ")
                generate_receipt(name, email, cart, total_cost, address)
            else:
                print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day!")
            break

if __name__ == "__main__":
    main()
