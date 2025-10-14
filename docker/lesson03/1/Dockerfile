FROM ubuntu:latest
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    pip install --break-system-packages flask
WORKDIR /app
ADD app.py /app/app.py
EXPOSE 80
CMD ["python", "app.py"]

