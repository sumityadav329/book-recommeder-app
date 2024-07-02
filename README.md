# Book Recommender Web App

## App Link

```url(https://book-recommender-app-3q48.onrender.com/)
```

## Overview

Welcome to the Book Recommender Web App! This project is designed to help users find book recommendations based on a selected book title. Using Natural Language Processing (NLP) techniques, we analyze the content of books to provide recommendations that are similar in theme and style to the book of your choice.

## Project Details

This project is part of an open internship at iNeuron Intelligence, conducted by Sumit Yadav (sumityad007gmail.com). The main objective of the project is to build a functional and user-friendly web application for book recommendations using Streamlit, a popular Python library for creating web apps.

## Features

- **Book Recommendations:** Get recommendations for books similar to your selected book title.
- **Data Processing:** Automated download and preprocessing of book data.
- **Model Training:** Training a TF-IDF Vectorizer and calculating cosine similarity scores for book recommendations.
- **Model Persistence:** Saving and loading trained models for efficient and quick recommendations.
- **Interactive Web Interface:** A beautiful, user-friendly interface built with Streamlit.

## Dataset

The dataset used for this project is a collection of book titles, authors, genres, and subgenres. The data is downloaded from a URL provided by iNeuron Internship Portal and preprocessed to extract meaningful features for recommendations.

## Technologies Used

- **Python:** The core programming language for the project.
- **Streamlit:** Used for creating the web interface.
- **scikit-learn:** Used for NLP and machine learning tasks.
- **Pandas:** Used for data manipulation and analysis.
- **Joblib:** Used for model persistence (saving and loading models).
## Project Structure

```
book-recommender-webapp/
│
├── artifacts/                       # Directory for storing downloaded data and trained models
│   ├── books.csv                    # Dataset of books
│   ├── vectorizer.pkl               # Trained TF-IDF vectorizer model
│   └── cosine_sim.pkl               # Trained cosine similarity matrix
│
├── src/                             # Source code directory
│   ├── __init__.py
│   ├── data_loader.py               # Module for downloading and loading data
│   ├── data_preprocessor.py         # Module for preprocessing data
│   ├── exception.py                 # Custom exception handling
│   ├── logger.py                    # Logging configuration
│   ├── model_loader.py              # Module for loading trained models
│   ├── model_saver.py               # Module for saving trained models
│   ├── model_trainer.py             # Module for training models
│   └── recommender.py               # Recommendation engine
│
├── app.py                           # Streamlit web app
├── setup.py                         # Setup this project as local package
├── template.py                      # Template for creating folder structure
├── test.py                          # Test script for testing the entire process
├── requirements.txt                 # Dependencies
├── Dockerfile                       # Docker configuration for deploying the app
└── README.md                        # Project README file
```

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/sumityadav329/book-recommender-app.git
    cd book-recommender-app
    ```

2. **Create a virtual environment and activate it**:
    ```bash
    python -m venv venv
    source venv/bin/activate    # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the App Locally

1. **Start the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

2. **Open your browser and navigate to** `http://localhost:8501` **to use the app**.

### Docker Deployment

1. **Build the Docker image**:
    ```bash
    docker build -t book-recommender-webapp .
    ```

2. **Run the Docker container**:
    ```bash
    docker run -p 8501:8501 book-recommender-webapp
    ```

## Detailed Project Workflow

1. **Data Downloading and Loading**: 
    - The app downloads the book dataset from a specified URL and saves it locally.
    - The dataset is then loaded into a pandas DataFrame for processing.

2. **Data Preprocessing**:
    - Missing values are filled.
    - Relevant features are combined into a single string to prepare for vectorization.

3. **Model Training**:
    - A TF-IDF Vectorizer converts the text data into numerical vectors.
    - A Cosine Similarity matrix is computed from these vectors to measure the similarity between books.

4. **Model Saving and Loading**:
    - Trained models (TF-IDF vectorizer and cosine similarity matrix) are saved to disk.
    - Models are loaded from disk when needed to avoid retraining.

5. **Recommendation Engine**:
    - The app uses the cosine similarity matrix to recommend books similar to the user's selected title.

6. **Streamlit Web App**:
    - Provides a user interface to input book titles and display recommendations.
    - Ensures a smooth and interactive user experience.

## Example Usage

1. Select or enter a book title in the search box.
2. Click on the "Get Recommendations" button.
3. View the recommended books displayed on the web page.

## Contact

For any queries or further information, feel free to contact:

**Sumit Yadav**  
Email: sumityad007@gmail.com  

Enjoy discovering new books with the Book Recommender Web App!


## Contributing

We welcome contributions! Please fork the repository and submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to the authors and maintainers of the libraries and datasets used in this project.
- Inspired by various book recommendation systems and machine learning tutorials.
- Special thanks to Mr. Krish Naik, Mr. Boktiar Ahmed Bappy, Mr. Sudhanshu Kumar.
---

Enjoy finding your next great read with our Book Recommender Web App! If you have any questions or feedback, feel free to reach out.

