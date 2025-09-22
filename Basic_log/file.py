import logging

# Configure logging to write to a file named 'app.log'
logging.basicConfig(filename='app.log', 
                    filemode='w', # 'w' for write (overwrite), 'a' for append
                    level=logging.INFO)

logging.info("The program started.")
logging.warning("An unusual event occurred.")
logging.info("The program is finishing.")

print("Log messages have been written to app.log")