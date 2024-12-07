# nk737-IS601-003

# Dose Restaurant API - Final Project

## Overview
This project is a REST API backend for a dose restaurant. The API provides access to three main entities: Customers, Items, and Orders. The backend uses FastAPI and SQLite as the database. This API allows for CRUD operations on the customers, items, and orders data.

## Features
- **Customer**: Create, retrieve, update, and delete customer records.
- **Item**: Create, retrieve, update, and delete item records.
- **Order**: Create, retrieve, update, and delete orders, (customers and items).
  
## Database
The database (`db.sqlite`) is initialized using SQLite and stores data in the following tables:
- **Customers**: Stores customer information, including name and phone number.
- **Items**: Stores menu items with their names and prices.
- **Orders**: Stores orders made by customers, with references to customer and item data.
- **OrderDetails**: Stores the relationship between orders and the items ordered.

## Project Setup

### Prerequisites

- Python 3.x
- SQLite
- FastAPI
- Uvicorn (for running the FastAPI app)

### Installation

1. Clone the repository:
   git clone https://github.com/NithinKrishna856-spec/nk737-IS601-003.git

2. Navigate to the project directory:
   cd nk737-IS601-003

3. Install the required dependencies:
   pip install -r requirements.txt

4. Initialize the database:
   - Run the following command to set up the database:
   python init_db.py

5. Start the FastAPI app:
   uvicorn main:app --reload
   The API will be available at `http://localhost:8000`.

### API Endpoints

#### **Customer Endpoints**

- **POST /customers**: Creates a new customer.
- **GET /customers/{id}**: Retrieve customer by ID.
- **DELETE /customers/{id}**: Delete a customer by ID.
- **PUT /customers/{id}**: Update a customer by ID.

#### **Item Endpoints**

- **POST /items**: Create a new item.
- **GET /items/{id}**: Retrieves item by ID.
- **DELETE /items/{id}**: Delete an item by ID.
- **PUT /items/{id}**: Update an item by ID.
  
#### **Order Endpoints**

- **POST /orders**: Create a new order.
 - **GET /orders/{id}**: Retrieves order by ID.
- **DELETE /orders/{id}**: Delete an order by ID.
- **PUT /orders/{id}**: Update an order by ID.
 
### Running Tests

To run tests on API, we can use pytest. We can run the tests using the following command:
pytest
