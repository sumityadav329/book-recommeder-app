# Use an official Python runtime as a parent image
FROM python:3.7.16-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that the application runs on
EXPOSE 8501

# Command to run the application
CMD ["streamlit", "run", "--server.enableCORS", "false", "app.py"]