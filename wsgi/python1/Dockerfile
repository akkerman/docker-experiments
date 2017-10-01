FROM python:3.6
LABEL maintainer "Marcel Akkerman <ikbenMarcelAkkerman@hotmail.com>"
RUN mkdir /app
WORKDIR /app
COPY ./requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
COPY ./*.py ./
COPY ./uwsgi.ini ./
CMD ["uwsgi", "--master", "uwsgi.ini"]

