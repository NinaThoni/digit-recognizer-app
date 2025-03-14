# Use an official Python image as the base
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the application files
COPY requirements.txt .
COPY frontend/ frontend/
COPY model/ model/
COPY database/ database/

# Install dependencies
RUN pip install -r requirements.txt

# Expose port for Streamlit
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "frontend/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
