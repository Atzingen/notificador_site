FROM python:3.12-slim

WORKDIR /app

# Install dependencies
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     libsqlite3-dev \
#     && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy application code
COPY . /app/

# Set environment variables from .env file
ENV PYTHONUNBUFFERED=1

# Run the bot
CMD ["python", "main.py"]