FROM python:3.12-alpine

WORKDIR /app

COPY app.py .
COPY templates ./templates

RUN pip install flask mysql-connector-python

EXPOSE 5000

CMD ["python", "app.py"]
