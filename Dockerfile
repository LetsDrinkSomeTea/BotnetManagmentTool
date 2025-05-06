# Use the official Python image as the base image
FROM python:3.9-alpine AS builder

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Use a smaller base image for the final image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files from the builder stage
COPY --from=builder /app /app

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME BotnetManagementTool

# Run main.py when the container launches
CMD ["python", "main.py", "-t", "10"]
