# Use the official Python image as the base image
FROM python:3.11-alpine

# Install Flask and other dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copy the code executor and the app into the container
COPY code_executor.py /apps/views.py
COPY apps /apps

# Set the working directory
WORKDIR /apps

# Expose the port for Flask
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
