# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /

# Copy the application files into the working directory
COPY . /src

# Install the application dependencies
RUN pip install -r src/requirements.txt

# Define the entry point for the container
CMD ["python", "runner.py"]