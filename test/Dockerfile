FROM python:3

COPY ./test_e2e.py /test/
COPY ./create.json /test/
COPY ./update.json /test/
COPY ./delete.json /test/

WORKDIR /test

RUN pip install requests && pip install requests && pip install pytest

CMD [ "bash" ]
ENTRYPOINT pytest -v -s
