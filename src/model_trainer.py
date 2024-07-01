import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.logger import logging
from src.exception import CustomException

def train_model(books_df):
    try:
        # Convert the text data into TF-IDF feature vectors
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(books_df['combined_features'])

        # Compute the cosine similarity matrix
        cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

        logging.info("Models trained successfully")
        return vectorizer, cosine_sim
    except Exception as e:
        logging.error(f"Error training models: {e}")
        raise CustomException(e, sys)
