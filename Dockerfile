# syntax=docker/dockerfile:1
FROM python:3.9
WORKDIR /code

RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "-m", "main"]