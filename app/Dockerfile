FROM python:3.14-slim
RUN pip install --upgrade pip setuptools wheel
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]