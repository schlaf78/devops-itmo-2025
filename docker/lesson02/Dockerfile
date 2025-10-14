FROM python:3.8
WORKDIR /app
RUN pip install flask
ADD app.py /app/app.py
EXPOSE 80
CMD ["python", "app.py"]
