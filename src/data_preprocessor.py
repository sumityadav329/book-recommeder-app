import pandas as pd
import sys
from src.logger import logging
from src.exception import CustomException

def preprocess_data(books_df: pd.DataFrame) -> pd.DataFrame:
    try:
        logging.info("Starting data preprocessing")

        # Fill missing values
        books_df.fillna('', inplace=True)

        # Combine relevant features into a single string
        books_df['combined_features'] = books_df.apply(
            lambda row: ' '.join([row['Title'], row['Author'], row['Genre'], row['SubGenre']]),
            axis=1
        )

        logging.info("Data preprocessing completed successfully")
        return books_df

    except Exception as e:
        logging.error(f"Error processing data: {e}")
        raise CustomException(e, sys)
