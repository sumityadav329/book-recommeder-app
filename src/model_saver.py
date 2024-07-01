import sys
import os
import joblib
from src.logger import logging
from src.exception import CustomException

def save_model(vectorizer, cosine_sim, save_dir):
    try:
        # Ensure the save directory exists
        os.makedirs(save_dir, exist_ok=True)

        vectorizer_path = os.path.join(save_dir, 'vectorizer.pkl')
        cosine_sim_path = os.path.join(save_dir, 'cosine_sim.pkl')
        
        # Save the models using joblib
        joblib.dump(vectorizer, vectorizer_path)
        joblib.dump(cosine_sim, cosine_sim_path)
        
        logging.info("Models saved successfully")
    except Exception as e:
        logging.error(f"Error saving models: {e}")
        raise CustomException(e, sys)
