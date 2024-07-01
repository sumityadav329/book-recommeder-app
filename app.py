from src.logger  import logging
from src.data_loader import download_data, load_csv
from src.exception import CustomException

def main():
    try:
        # URL for downloading data
        data_url = 'https://gist.githubusercontent.com/jaidevd/23aef12e9bf56c618c41/raw/c05e98672b8d52fa0cb94aad80f75eb78342e5d4/books_new.csv'
        data_save_path = 'artifacts/books.csv'
        download_data(data_url, data_save_path)

        # Loading the CSV file
        df = load_csv(data_save_path)

    except CustomException as e:
        logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
