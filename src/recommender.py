from src.logger import logging
from src.exception import CustomException



# Function to get recommendations
def get_recommendations(title, cosine_sim, df):
    try:
        # Get the index of the book that matches the title
        idx = df[df['Title'] == title].index[0]

        # Get the pairwise similarity scores of all books with that book
        sim_scores = list(enumerate(cosine_sim[idx].flatten()))

        # Sort the books based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the 10 most similar books (excluding itself)
        sim_scores = sim_scores[1:11]

        # Get the book indices
        book_indices = [i[0] for i in sim_scores]

        # Return the top 10 most similar book titles
        return df['Title'].iloc[book_indices].tolist()

    except IndexError:
        logging.error(f"Book '{title}' not found in the dataset.")
        raise CustomException(f"Book '{title}' not found in the dataset.")
    except Exception as e:
        logging.error(f"Error getting recommendations: {e}")
        raise CustomException(f"Error getting recommendations: {e}")
