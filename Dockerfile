FROM python:3.7-alpine3.9

RUN apk add --no-cache --virtual .build-deps gcc musl-dev
ADD . /src
WORKDIR /src
RUN pip install -r requirements.txt
RUN apk del .build-deps gcc musl-dev


EXPOSE 5000
ENTRYPOINT ["python", "src/app.py"]