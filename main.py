from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
app = FastAPI()

def connect_database():
    return sqlite3.connect("db.sqlite", factory=sqlite3.Row)
class Customerr(BaseModel):
    name: str
    phone: str

# CRUD operations for customers 

@app.post("/customers", status_code = 201)
def create_customer(customer: Customerr):
    with connect_database() as con:
        cursor = con.cursor()
        cursor.execute("Insert into customers(name, phone) VALUES(?, ?)", (customer.name, customer.phone))
        con.commit()
        return {"id": cursor.lastrowid, "message": "Created customer"}
    

@app.get("/customers/{id}")
def retrieve_customer(id: int):
    with connect_database() as con:
        cursor = con.cursor()
        customer = cursor.execute("Select * from customers where id = ?", (id,)).fetchone()    
        if customer is None:
            return{"error": "No Customer found"}
        return dict(customer)


@app.delete("/customers/{id}")
def remove_customer(id: int):    
    with connect_database() as con:
        cursor = con.cursor()
        cursor.execute("Delete from customers where id = ?", (id,))
        con.commit()
        return{"message": "Deleted Customer"}
    
@app.put("/customers/{id}")
def update_customer(id: int, customer: Customerr):
    with connect_database() as con:
        cursor = con.cursor()
        cursor.execute(
        "Update customers set name = ?, phone = ? where id = ?", (customer.name, customer.phone, id))
        con.commit()
        return {"message": "Customer updated"}

    
# CRUD operations on items

@app.post("/items")
def create_item(item: dict):
    with connect_database() as con:
        cursor = con.cursor()
        cursor.execute("Insert into Items(name, price) values(?, ?)", (item["name"], item["price"]))
        con.commit()
        return {"id": cursor.lastrowid, "message": "Created Item"}

@app.get("/items/{id}")
def retrieve_item(id: int):
    with connect_database() as con:
        cursor = con.cursor()
        item = cursor.execute("Select * from Items where id = ?", (id,)).fetchone()
        if item is None:
            return {"error": "No Item found"}
        return dict(item)

@app.delete("/items/{id}")
def remove_item(id: int):
    with connect_database() as con:
        cursor = con.cursor()
        cursor.execute("Delete from Items where id = ?", (id,))
        con.commit()
        return {"message": "Deleted Item"}

@app.put("/items/{id}")
def update_item(id: int, item: dict):
    with connect_database() as con:
        cursor = con.cursor()
        cursor.execute("Update Items set name = ?, price = ? where id = ?", (item["name"], item["price"], id))
        con.commit()
        return {"message": "Item updated"}



#CRUD operations on orders

@app.post("/orders")
def create_order(order: dict):
    with connect_database() as con:
        cursor = con.cursor()
        cursor.execute("Insert into Orders(customer_id, timestamp, notes) values(?,?,?)", (order["customer_id"], order["timestamp"], order.get("notes", "")))
        order_id = cursor.lastrowid
        for item_id in order["item_ids"]:
            cursor.execute("Insert into OrderDetails (order_id, item_id) values(?, ?)", (order_id, item_id))
        con.commit()
        return{"id": order_id, "message":"Created Order"}

@app.get("/orders/{id}")
def retrieve_order(id: int):
    with connect_database() as con:
        cursor = con.cursor()
        order = cursor.execute("Select * from Orders where id = ?", (id,)).fetchone()
        if order is None:
            return {"error": "No Order found"}
        items = cursor.execute("Select i.id, i.name, i.price from OrderDetails od join Items i ON od.item_id = i.id WHERE od.order_id = ?", (id,)).fetchall()
        return {"order": dict(order), "items": [dict(item) for item in items]}
    
@app.delete("/orders/{id}")
def remove_order(id: int):
    with connect_database() as con:
        cursor = con.cursor()
        cursor.execute("Delete from OrderDetails where order_id = ?", (id,))
        cursor.execute("Delete from Orders where id = ?", (id,))
        con.commit()
        return {"message": "Deleted Order"}

@app.put("/orders/{id}")
def update_order(id: int, order: dict):
    with connect_database() as con:
        cursor = con.cursor()
        cursor.execute("Update Orders set customer_id = ?, timestamp = ?, notes = ? where id = ?", (order["customer_id"], order["timestamp"], order.get("notes", ""), id))
        cursor.execute("Delete from OrderDetails where order_id = ?", (id,))
        for item_id in order["item_ids"]:
            cursor.execute("Insert into OrderDetails(order_id, item_id) values(?, ?)", (id, item_id))
        con.commit()
        return {"message": "Order updated"}



