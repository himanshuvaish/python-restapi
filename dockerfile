# Use an official Python runtime as a parent image
FROM python:3.12-rc-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN /bin/bash -c "pip3 install --no-cache-dir -r requirements.txt"

# Install Flask
RUN /bin/bash -c "pip3 install Flask"

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask application
CMD ["flask", "run"]