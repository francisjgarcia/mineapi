FROM python:3.11.2-alpine3.17

LABEL maintainer Francis J. Garcia <contacto@francisjgarcia.es>
LABEL org.opencontainers.image.source="https://github.com/francisjgarcia/mineapi"
LABEL org.opencontainers.image.description "API written in Python with Django and Django REST Framework to manage resources of a Minecraft server"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN addgroup -S python && adduser -S python -G python

USER python:python

WORKDIR /usr/src/app

COPY --chown=python:python app .

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "python", "manage.py" ]

CMD [ "runserver", "0.0.0.0:8000" ]
