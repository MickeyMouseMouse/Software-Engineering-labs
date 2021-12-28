FROM python:3.10-slim-buster
RUN pip3 install beautifulsoup4 requests
WORKDIR Task1
ADD converter.py .
ENTRYPOINT ["python", "./converter.py"]
