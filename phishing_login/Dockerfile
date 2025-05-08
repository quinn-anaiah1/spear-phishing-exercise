FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install flask --no-cache-dir --progress-bar off
EXPOSE 80
CMD ["python3", "app.py"]

