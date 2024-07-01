import os
import sys
import joblib
from src.logger import logging
from src.exception import CustomException

def load_models(model_paths: dict) -> dict:
    models = {}
    try:
        for model_name, model_path in model_paths.items():
            logging.info(f"Loading model '{model_name}' from {model_path}")
            with open(model_path, 'rb') as file:
                models[model_name] = joblib.load(file)
            logging.info(f"Model '{model_name}' loaded successfully")
        return models
    except Exception as e:
        logging.error(f"Error loading models: {e}")
        raise CustomException(e, sys)
