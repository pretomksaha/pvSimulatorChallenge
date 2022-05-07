FROM python:3

ADD . ./code

RUN apt clean
RUN apt-get update
RUN apt-get install -y --no-install-recommends
WORKDIR /code/


COPY requirements.txt .
RUN pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

COPY . ./code
CMD ["python", "-m", "App/main.py"]