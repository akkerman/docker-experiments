FROM python:3.6
LABEL maintainer "Marcel Akkerman <ikbenMarcelAkkerman@hotmail.com>"

CMD mkdir /app
WORKDIR /app

COPY ./requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY *.py ./
CMD ["python", "-u", "mqttc2.py"]
