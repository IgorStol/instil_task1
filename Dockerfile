FROM python:3.8

RUN pip install flask

COPY calc.py Users/ee/Documents/docker/calc.py

WORKDIR /Users/ee/Documents/docker

CMD ["python", "calc.py"]