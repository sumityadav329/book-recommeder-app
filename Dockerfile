# Use an official Python runtime as a parent image
FROM python:3.7.16-slim

# Set the working directory in the container
WORKDIR /app

# Install virtualenv package
RUN pip install virtualenv

# Create a virtual environment
RUN virtualenv venv

# Activate the virtual environment and install any needed packages specified in requirements.txt
COPY requirements.txt .
RUN . venv/bin/activate && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that the application runs on
EXPOSE 8501

# Define environment variable
ENV NAME BookRecommender

# Create an empty .project-root file to signal the root directory
RUN touch .project-root

# Command to run the application inside the virtual environment
CMD ["sh", "-c", ". venv/bin/activate && streamlit run --server.enableCORS false app.py"]
