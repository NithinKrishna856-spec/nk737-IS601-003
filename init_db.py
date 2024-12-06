import sqlite3
import os

def initializing_db():
    db_file = "db.sqlite"
    if os.path.exists(db_file):
        os.remove(db_file)
        print(f"Deleted existing database file: {db_file}")
        
    conn = sqlite3.connect("db_file")
    cursor = conn.cursor()

    # here we create the tables
    cursor.execute("""create table if Not exists Customers (id Integer Primary Key Autoincrement, name Text Not Null, phone Text Not Null Unique)""")

    cursor.execute("""create table if Not exists Items (id Integer Primary Key Autoincrement, name Text Not Null, price Decimal Not Null)""")

    cursor.execute("""create table if Not exists Orders (id Integer Primary Key Autoincrement, customer_id Integer Not Null, timestamp Integer Not Null, Notes Text, Foreign Key (customer_id) References Customers (id))""")

    cursor.execute("""create table if Not exists OrderDetails (order_id Integer Not Null, item_id Integer Not Null, Foreign Key (order_id) References Orders (id), Foreign Key (item_id) References Items (id), Primary Key (order_id, item_id))""")

    

    conn.commit()
    conn.close()
    print("Empty database initialized successfully.")

if __name__ == "__main__":
    initializing_db()
