# Initialize the menu, orders, and unique customers
menu = {
    "Pizza": (12.99, "Main Course"),
    "Burger": (8.99, "Main Course"),
    "Pasta": (10.99, "Main Course"),
    "Salad": (6.99, "Appetizer"),
    "Soda": (1.99, "Beverage"),
    "Ice Cream": (4.99, "Dessert")
}

orders = []  # List to store all orders
unique_customers = set()  # Set to store unique customer names

# Function to display the menu
def display_menu():
    print("Menu:")
    for item, (price, category) in menu.items():
        print(f"{item}: ${price:.2f} ({category})")

# Function to place an order
def place_order(customer_name, item_list):
    order_id = len(orders) + 1  # Generate a unique order ID
    total_bill = sum(menu[item][0] for item in item_list)  # Calculate total bill
    order = (order_id, customer_name, item_list, total_bill)  # Create order tuple
    orders.append(order)  # Add order to the list
    unique_customers.add(customer_name)  # Add customer to the set of unique customers
    print(f"Order placed successfully! Order ID: {order_id}, Total Bill: ${total_bill:.2f}")

# Function to generate a bill for a specific order
def generate_bill(order_id):
    for order in orders:
        if order[0] == order_id:
            print(f"Bill for Order ID {order_id}:")
            print(f"Customer Name: {order[1]}")
            print("Items Ordered:")
            for item in order[2]:
                print(f"- {item}: ${menu[item][0]:.2f}")
            print(f"Total Bill: ${order[3]:.2f}")
            return
    print(f"Order ID {order_id} not found!")

# Function to display total revenue generated
def display_total_revenue():
    total_revenue = sum(order[3] for order in orders)
    print(f"Total Revenue Generated: ${total_revenue:.2f}")

# Function to display unique customers
def display_unique_customers():
    print("Unique Customers Who Placed Orders:")
    for customer in unique_customers:
        print(f"- {customer}")

# Main program
if __name__ == "__main__":
    # Display the menu
    display_menu()

    # Place sample orders
    place_order("Alice", ["Pizza", "Soda"])
    place_order("Bob", ["Burger", "Salad", "Ice Cream"])
    place_order("Alice", ["Pasta", "Soda"])

    # Generate a bill for a specific order
    generate_bill(1)

    # Display total revenue
    display_total_revenue()

    # Display unique customers
    display_unique_customers()