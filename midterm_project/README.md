# Dose Restaurant Orders System

This project manages order data for a Dose restaurant. It reads a JSON file of past orders, extracts customer and item data, and generates two JSON files `customers.json` and `items.json`.

## Design

The project is designed as follows:
1. **Reading JSON Orders**: The script reads a JSON file containing restaurant orders as input. This file is provided as a command-line argument.
2. **Extracting Customer Data**: The script extracts customer phone numbers and names from the orders and saves them in `customers.json`.
3. **Extracting Item Data**: The script extracts item names, prices, and the number of times each item has been ordered from the orders. This data is saved in `items.json`.
4. **Output Files**:
    - `customers.json`: Contains customer phone numbers as keys and customer names as values.
    - `items.json`: Contains item names as keys and an object with `price` and `orders` as values.

## How to Run

To run the script, you need to have Python installed. 
- Verify if Python is already installed by running the following command in your terminal or command prompt:
    ```bash
    python --version
    ```
- If Python is not installed, download and install it from the [official Python website](https://www.python.org/downloads/).
- Clone the repository containing the project files:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```
- Change to the directory where the script is located (e.g., `midterm_project`):
    ```bash
    cd midterm_project
    ```

The script takes a JSON file of orders as input. The example file provided is `example_orders.json`.

### Command to Run the Script

```bash
python dose_orders.py example_orders.json
```

### Expected Output

After running the script, two JSON files will be generated in the same directory:
- **customers.json**: This file will contain an object where phone numbers are keys and customer names are values. 
- **items.json**: This file will have item names as keys, and each key will have an object containing the item’s price and the number of times it has been ordered. 

### Troubleshooting
If you run into any issues while executing the script, here are a few things to check:

- Make sure the JSON file is present in the specified location and that it’s properly formatted.
- Double-check that you’re in the right directory where the script is located.
- Confirm that the command you typed is correct and that the filenames match exactly, paying attention to    any uppercase or lowercase letters.
By going through these steps, you should be able to run the script successfully and create the output files you need.

