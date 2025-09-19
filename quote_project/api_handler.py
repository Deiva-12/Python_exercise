# api_handler.py
import requests
import logging

logging.basicConfig(level=logging.INFO,
                    filename= "api_file.log",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def get_random_quote():
    """Fetches a random quote from the quotable.io API."""
    try:
        response = requests.get("https://quotes-api-self.vercel.app/quote")
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()
        #print(response)
        logger.info(response)

        data = response.json()
        author = data['author']
        quote = data['quote']
        logger.info(author)
        return f'"{author}" - {quote}'
        # return data
    except requests.exceptions.RequestException as e:
        return f"Error: Could not fetch a quote. Please check your internet connection. Details: {e}"
    