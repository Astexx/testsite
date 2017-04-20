# Use an official Python runtime as a base image
FROM python:2.7-slim

# Set the working directory
WORKDIR /tests

# Copy the current directory contents into the container
ADD . /tests

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run tests with robot when the container launches
CMD ["robot", "./"]
