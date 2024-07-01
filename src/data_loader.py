import os
import requests
import sys
import pandas as pd
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

def load_csv(file_path: str) -> pd.DataFrame:
    try:
        logging.info(f"Loading CSV file from {file_path}")
        df = pd.read_csv(file_path)
        logging.info(f"CSV file loaded successfully")
        return df
    except Exception as e:
        logging.error(f"Error loading CSV file: {e}")
        raise CustomException(e, sys)
