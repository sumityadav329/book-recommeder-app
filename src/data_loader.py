import os
import requests
import sys
from src.exception import CustomException
from src.logger  import logging

def download_data(url: str, save_path: str):
    try:
        logging.info(f"Downloading data from {url}")
        response = requests.get(url)
        with open(save_path, 'wb') as file:
            file.write(response.content)
        logging.info(f"Data downloaded successfully and saved to {save_path}")
    except Exception as e:
        logging.error(f"Error downloading data: {e}")
        raise CustomException(e, sys)

