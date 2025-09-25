import logging

# Configure the logging system
logging.basicConfig(level=logging.INFO)

logging.debug("This message will NOT be shown, because the level is INFO.")
logging.info("This message WILL now be shown.")
logging.warning("This one will also be shown.")