from src.logger import logging
from src.data_loader import download_data, load_csv
from src.data_preprocessor import preprocess_data
from src.model_loader import load_models
from src.model_trainer import train_model
from src.model_saver import save_model
from src.exception import CustomException

def main():
    try:
        # URL for downloading data
        data_url = 'https://gist.githubusercontent.com/jaidevd/23aef12e9bf56c618c41/raw/c05e98672b8d52fa0cb94aad80f75eb78342e5d4/books_new.csv'
        data_save_path = 'artifacts/books.csv'
        download_data(data_url, data_save_path)

        # Load the data from the CSV file
        books_df = load_csv(data_save_path)

        # Preprocess the data
        processed_books_df = preprocess_data(books_df)

        # Train the model
        vectorizer, cosine_sim = train_model(processed_books_df)

        # Save the trained models
        save_model(vectorizer, cosine_sim, 'artifacts')

        # Paths to your models
        model_paths = {
            'vectorizer': 'artifacts/vectorizer.pkl',
            'cosine_sim': 'artifacts/cosine_sim.pkl'
        }

        # Load the models
        models = load_models(model_paths)

        # Access the models
        vectorizer = models['vectorizer']
        cosine_sim = models['cosine_sim']

    except CustomException as e:
        logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
