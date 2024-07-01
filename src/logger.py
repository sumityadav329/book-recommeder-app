import logging
import os
from datetime import datetime
from from_root import from_root

# Define log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define log directory path
log_dir = os.path.join(from_root(), 'logs')

# Create log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Define full log file path
LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s ",
    level=logging.INFO
)

# Optional: Set up a console handler to see logs in the console as well
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s "))
logging.getLogger().addHandler(console_handler)
