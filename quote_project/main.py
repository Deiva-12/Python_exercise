# main.py
import logging
from api_handler import get_random_quote

# logging.basicConfig(level=logging.INFO,
#                     filename="main.log",
#                     format=' %(asctime)s - %(name)s - %(levelname)s - %(message)s')


# TODO: Import the get_random_quote function from the api_handler file.



# TODO: Call the function and store the result in a variable named 'quote'.
quote = get_random_quote() 

# Print the final quote
print("--- Your Inspirational Quote of the Day ---")
print(quote)
logging.info("Main application is finished") # TODO: Uncomment this line after you've defined the 'quote' variable