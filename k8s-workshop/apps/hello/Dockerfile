
# Use an official, lightweight Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first to leverage Docker's build cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the web app runs on (e.g., 5000 for Flask, 8000 for FastAPI)
EXPOSE 8080

# Run the web application using a production WSGI/ASGI server (like Gunicorn or Uvicorn)
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "--threads", "4", "app:app"]