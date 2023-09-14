# Use the base image of Python
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your code into the container
COPY . .

# Install the required dependencies
RUN pip install -r requirements.txt

# Indicate that the container is listening on port 5000
EXPOSE 8080

# Define the command to run when the container starts
CMD ["python", "testTwilio.py"]
