# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set a working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies (you might need to adjust this list based on your requirements)
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8501 for Streamlit app
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py"]
