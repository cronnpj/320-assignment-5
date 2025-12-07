FROM python:3.10-slim

WORKDIR /app
COPY . /app

# Install required Python packages
RUN pip install flask requests

CMD ["python", "app.py"]
