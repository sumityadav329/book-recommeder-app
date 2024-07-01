import streamlit as st
from src.recommender import get_recommendations
from src.data_loader import download_data, load_csv
from src.data_preprocessor import preprocess_data
from src.model_loader import load_models
from src.model_trainer import train_model
from src.model_saver import save_model
from src.exception import CustomException


def main():
    st.title('Book Recommender System')

    try:
        # URL for downloading data
        data_url = 'https://gist.githubusercontent.com/jaidevd/23aef12e9bf56c618c41/raw/c05e98672b8d52fa0cb94aad80f75eb78342e5d4/books_new.csv'
        data_save_path = 'artifacts/books.csv'

        # Download and load the data
        download_data(data_url, data_save_path)
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
        vectorizer = models['vectorizer']
        cosine_sim = models['cosine_sim']

        # Selectbox for book title
        user_input = st.selectbox('Select a book title:', processed_books_df['Title'].values)

        # Button to get recommendations
        if st.button('Get Recommendations'):
            recommendations = get_recommendations(user_input, cosine_sim, processed_books_df)
            if recommendations:
                st.success("Here are 10 book recommendations:")
                for book in recommendations:
                    st.write(book)
            else:
                st.warning("No recommendations found.")

    except CustomException as e:
        st.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
