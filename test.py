import logging
from src.logger import logging
from src.exception import CustomException
import sys

# Trigger an error and catch it to test logging and custom exception
def test_logging_and_exception():
    try:
        # Simulate a division by zero error
        x = 1 / 0
    except Exception as e:
        # Log the error
        logging.error("An error occurred: %s", str(e))

        # Raise a custom exception
        raise CustomException(e, sys)

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    
    try:
        test_logging_and_exception()
    except CustomException as ce:
        # Print the custom exception message
        print(str(ce))
