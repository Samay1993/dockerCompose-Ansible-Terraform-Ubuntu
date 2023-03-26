# Use the official Python image as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container and install the dependencies
COPY /app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .
# Expose port 4000 for the Flask application
EXPOSE 4000

# Start the Flask application when the container starts
CMD [ "python", "main.py" ]
