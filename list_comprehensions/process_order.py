import json
import logging

logging.basicConfig(level=logging.INFO)
# Read the JSON file in try/except block, parse it into a Python dictionary and log the dictionary variable

## Your code here
try:
    with open('order_data.json', 'r') as file:
        data = json.load(file)
        
        # The JSON's top-level object is a dictionary, and our list is inside the "employees" key.
        
except FileNotFoundError:
    print("Error: order_data.json not found. Please create the file.")
    product = []

# --- Accessing Nested Fields ---

# Access a top-level field "order_id" and log using info level
## Your code here

logging.info(f"Processing Order ID : {data['order_id']}")




# Access a field within a nested object, (customer --> name) and (customer -> address -> city). Log using info level
## Your code here
# print(data["customer"]["name"])
# print(data["customer"]["address"]['city'])
logging.info(f"Customer : {data["customer"]["name"]} from {data["customer"]["address"]['city']} ")




# --- Processing a Nested List ---
# Get total cost of the all the items and log the total billing amount
total_cost = 0.0
items = data.get("items", [])
for item in items:
    # print(f"Product_name : {item['product_name']} "  f"Price: {item['price']}"  )
    total_vale = item["quantity"] * item["price"]
    total_cost+=total_vale
    print("\nOrder Items:")
    logging.info(f"Product_name : {item['product_name']}" f" - {item['price']}")
logging.info(f"Total cost : {total_cost}")
    

    




# The 'items' key holds a list of dictionaries
## Your code here

    
