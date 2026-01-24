FROM python:3.12-bookworm

# Set working directory
WORKDIR /app

# Copy current directory into app directory
COPY . /app

# Install all dependencies
RUN pip install -r requirements.txt

CMD ["python", "app.py"]