import json  
import sys   # Importing sys to handle command-line arguments and exits

# Function to read orders from a JSON file
def read_orders(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)  # Parse the JSON data into a Python object
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        sys.exit(1)

# Function to extract customer information from the orders
def extract_customers(orders):
    customers = {}  
    for order in orders:
        phone = order.get('phone')  # Extract customer phone number from each order
        name = order.get('name')     # Extract customer name from each order
        if phone and name:  # Check if both fields are present
            customers[phone] = name
        else:
            print("Missing phone or name in order:", order)
    return customers  

# Function to write customer data to a file (customers.json)
def write_customers(customers):
    with open('customers.json', 'w') as file:
        json.dump(customers, file, indent=4)

# Function to extract item information from the orders
def extract_items(orders):
    items = {}  
    for order in orders:
        for item in order.get('items', []):  # Default an empty list if items are missing
            item_name = item.get('name')  # Extract item name
            item_price = item.get('price')  # Extract item price
            if item_name and item_price:  # Check if both fields are present
                if item_name not in items:
                    items[item_name] = {  # Properly indent this block
                        'price': item_price, 
                        'orders': 0  # Initialize order count 
                    }
                items[item_name]['orders'] += 1  # Increment the count of how many times the item was ordered
            else:
                print("Missing name or price in item:", item)
    return items  

# Function to write item data to a file (items.json)
def write_items(items):
    with open('items.json', 'w') as file:
        json.dump(items, file, indent=4)

if __name__ == "__main__":
    # Check if the user provided the JSON file name as an argument
    if len(sys.argv) < 2:
        print("Please provide the orders JSON file name.")  
        sys.exit(1)  
    orders = read_orders(sys.argv[1])
    customer_info = extract_customers(orders)
    write_customers(customer_info)
    item_info = extract_items(orders)
    write_items(item_info)
    print("Data has been successfully extracted and written to 'customers.json' and 'items.json'.")
