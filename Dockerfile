FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /srv/www
WORKDIR /srv/www
ADD requirements.txt /srv/www/
RUN pip install -r requirements.txt
ADD . /srv/www/