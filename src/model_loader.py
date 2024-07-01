import gdown
import os
from src.logger import logging
from src.exception import CustomException 

def download_models_from_gdrive(urls, save_dir):
    try:
        os.makedirs(save_dir, exist_ok=True)
        
        for name, url in urls.items():
            save_path = os.path.join(save_dir, name)
            logging.info(f"Downloading {name} from Google Drive: {url}")
            gdown.download(url, save_path, quiet=False)
            logging.info(f"Downloaded {name} successfully to: {save_path}")
        
        logging.info(f"All models downloaded successfully to {save_dir}")
        
    except Exception as e:
        logging.error(f"Error downloading models: {e}")
        raise CustomException(e)


