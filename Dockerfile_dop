# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Make start script executable
RUN chmod +x start.sh

# Expose ports
# 8000 for FastAPI, 8501 for Streamlit
EXPOSE 8000 8501

# Run both services
# API available at port 8000, Dashboard at port 8501
CMD ["./start.sh"]
