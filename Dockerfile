# syntax=docker/dockerfile:1
FROM python:3.9
WORKDIR /code

RUN pip install -r requirements.txt
COPY . .
CMD ["python", "-m", "main"]