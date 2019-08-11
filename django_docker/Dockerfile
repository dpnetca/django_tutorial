FROM python:3.7-alpine

# set environment variables
# from https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create working directoy and copy requirements
WORKDIR /app
COPY requirements.txt /app/requirements.txt

# install psycopg2, create python venv and install requirements
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del build-deps \
    && rm -rf /var/cache/apk/*

# expose port 8000
# EXPOSE 8000

COPY /django_docker/ /app/

# run entrypoint.sh
ENTRYPOINT [ "/app/entrypoint.sh" ]
