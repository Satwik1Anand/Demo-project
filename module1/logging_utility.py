import logging

# Set up basic configuration for logging
logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Define a function to log messages

def log_message(message):
    logging.debug(message)
    
# Testing the logging function
if __name__ == '__main__':
    log_message('Logging utility initialized.')