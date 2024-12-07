import sqlite3
import os
import json

def initializing_db():
    db_file = "db.sqlite"
    if os.path.exists(db_file):
        os.remove(db_file)
        print(f"Deleted existing database file: {db_file}")
        
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create the tables
    cursor.execute("""create table if Not exists Customers (id Integer Primary Key Autoincrement, name Text Not Null, phone Text Not Null Unique)""")
    cursor.execute("""create table if Not exists Items (id Integer Primary Key Autoincrement, name Text Not Null, price Decimal Not Null)""")
    cursor.execute("""create table if Not exists Orders (id Integer Primary Key Autoincrement, customer_id Integer Not Null, timestamp Integer Not Null, Notes Text, Foreign Key (customer_id) References Customers (id))""")
    cursor.execute("""create table if Not exists OrderDetails (order_id Integer Not Null, item_id Integer Not Null, Foreign Key (order_id) References Orders (id), Foreign Key (item_id) References Items (id), Primary Key (order_id, item_id))""")

    # Load data from the example JSON file
    with open("example_orders.json", "r") as file:
        data = json.load(file)

    # Insert Customers and Items
    customers = {}
    items = {}

    for order in data:
        customer_name = order["name"]
        customer_phone = order["phone"]
        
        # Insert customer if not already in the dictionary
        if customer_name not in customers:
            cursor.execute("INSERT INTO Customers (name, phone) VALUES (?, ?)", (customer_name, customer_phone))
            customers[customer_name] = cursor.lastrowid
        
        # Insert Items
        for item in order["items"]:
            item_name = item["name"]
            item_price = item["price"]
            
            if item_name not in items:
                cursor.execute("INSERT INTO Items (name, price) VALUES (?, ?)", (item_name, item_price))
                items[item_name] = cursor.lastrowid
        
        # Insert the order
        customer_id = customers[customer_name]
        cursor.execute("INSERT INTO Orders (customer_id, timestamp, Notes) VALUES (?, ?, ?)", (customer_id, order["timestamp"], order["notes"]))
        order_id = cursor.lastrowid
        
        # Insert OrderDetails
        for item in order["items"]:
            item_name = item["name"]
            item_id = items[item_name]
            
            # Check if the order_id and item_id pair already exists in OrderDetails
            cursor.execute("SELECT 1 FROM OrderDetails WHERE order_id = ? AND item_id = ?", (order_id, item_id))
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO OrderDetails (order_id, item_id) VALUES (?, ?)", (order_id, item_id))

    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
    initializing_db()
