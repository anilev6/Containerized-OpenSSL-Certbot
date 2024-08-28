# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Copy the keys and certificates into the container
COPY secret.py /usr/src/app/
COPY main.py /usr/src/app/
COPY ssl/ /usr/src/app/ssl/

# Set the working directory in the container
WORKDIR /usr/src/app

# Run application when the container launches
CMD ["python", "main.py"]
