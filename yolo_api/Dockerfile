# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set a working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies (you might need to adjust this list based on your requirements)
RUN pip install --no-cache-dir -r requirements.txt


# RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# Expose port 80 for Flask API
EXPOSE 80

# Command to run the Flask app
CMD ["python", "app.py"]
