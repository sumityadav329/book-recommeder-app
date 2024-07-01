from src.logger  import logging
from src.data_loader import download_data, load_csv
from src.model_loader import download_models_from_gdrive
from src.exception import CustomException

def main():
    try:
        # URL for downloading data
        data_url = 'https://gist.githubusercontent.com/jaidevd/23aef12e9bf56c618c41/raw/c05e98672b8d52fa0cb94aad80f75eb78342e5d4/books_new.csv'
        data_save_path = 'artifacts/books.csv'
        download_data(data_url, data_save_path)

        # Loading the CSV file
        df = load_csv(data_save_path)

        # Dictionary of model names and their corresponding Google Drive URLs
        model_urls = {
            'vectorizer.pkl': 'https://drive.google.com/file/d/1uCCaB-gIFMZjY4abRS05ntAoZsSt2JMz/view?usp=sharing',
            'cosine_sim.pkl': 'https://drive.google.com/file/d/1_xQac2HdebaB_AddOMWURWxB54i7dePs/view?usp=sharing'
        }
        
        # Directory to save downloaded files
        save_directory = './artifacts'
        
        # Download the models
        download_models_from_gdrive(model_urls, save_directory)
    


    except CustomException as e:
        logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()