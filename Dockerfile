# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /NewtownHousePriceAPI

# Install dependencies
COPY requirement.txt .
RUN pip install --upgrade pip
RUN pip install -r requirement.txt

# Copy project
COPY . .

# Expose port
EXPOSE 8000

# Command to run the app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]