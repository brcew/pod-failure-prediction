# Use official Python image
FROM python:3.10-slim

# Create working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project
COPY . .

# Expose the port Streamlit will run on
EXPOSE 7860

# Make start.sh executable
RUN chmod +x start.sh

# Start the app
CMD ["./start.sh"]
