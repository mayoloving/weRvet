FROM python:3.6

WORKDIR /usr/src/app

COPY ./app ./

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT python3 ./weRvet.py