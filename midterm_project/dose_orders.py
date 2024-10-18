import json
import sys

def read_orders(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)
    
def extract_customers(orders):
    customers = {}
    for order in orders:
        phone = order['phone']
        name = order['name']
        customers[phone] = name
    return customers

def write_customers(customers):
    with open('customers.json', 'w') as file:
        json.dump(customers, file, indent=4)

def extract_items(orders):
    items = {}
    for order in orders:
        for item in order['items']:
            item_name = item['name']
            item_price = item['price']
            if item_name not in items:
                items[item_name] = {
                    'price': item_price,
                    'orders': 0
                }
            items[item_name]['orders'] += 1
    return items

def write_items(items):
    with open('items.json', 'w') as file:
        json.dump(items, file, indent=4)
    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the orders JSON file name.")
        sys.exit(1)

    orders = read_orders(sys.argv[1])
    customers = extract_customers(orders)
    write_customers(customers)
    
    items = extract_items(orders)
    write_items(items)

    print("Customer and item data have been written to JSON files.")
