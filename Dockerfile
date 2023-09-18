# Use the official Python image as the base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install any needed dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the entire project to the container
COPY . .

# Expose the port that FastAPI will run on
EXPOSE 8000

# Mount the resources and javascript directories as stpip installatic directories
# Adjust the paths according to your directory structure
RUN mkdir -p /app/frontend/resources
RUN mkdir -p /app/frontend/javascript
COPY frontend/resources /app/frontend/resources
COPY frontend/javascript /app/frontend/javascript

# Start the FastAPI application
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
