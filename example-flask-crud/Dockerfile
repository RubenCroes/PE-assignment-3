FROM python:3.11-slim

# Set working directory
WORKDIR /usr/src/app

# Install system dependencies for MySQL client and build tools
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt first (for better caching)
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 8000 for Gunicorn
EXPOSE 8000

RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
