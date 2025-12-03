# Simple Python base image
FROM python:3.12-slim

# Create app directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose port
EXPOSE 8000

# Optional healthcheck (simple)
HEALTHCHECK CMD curl -f http://localhost:8000/health || exit 1

# Start FastAPI app using uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
