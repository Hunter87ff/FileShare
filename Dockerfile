# Use the official Python image as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app
# Copy the application files into the working directory
COPY . /app
# Install the application dependencies
RUN pip install -r src/requirements.txt
EXPOSE 8787/http
# Define the entry point for the container
CMD ["python", "runner.py"]