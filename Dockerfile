# Use official Python 3.11 slim image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=7860

# Set working directory inside container
WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files (including app.py, start_docker.py, bot.py, etc.)
COPY . .

# Set permission for HF non-root user (Hugging Face runs as user 1000)
RUN chmod -R 777 /code

# Expose Hugging Face Space port
EXPOSE 7860

# Execute python script to run both background bot and frontend streamlit
CMD ["python3", "start_docker.py"]
