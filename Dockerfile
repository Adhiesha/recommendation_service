# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy everything
COPY requirements.txt .
COPY app ./app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables (optional if using .env)
ENV PYTHONPATH=/app

# Expose Flask app port
EXPOSE 5002

# Run the app using module path to app/run.py
CMD ["python", "-m", "app.run"]
