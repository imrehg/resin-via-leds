FROM resin/vab820-quad-python:3

WORKDIR /usr/src/app
ENV INITSYSTEM on

COPY requirements.txt .
RUN pip install -vvv -r requirements.txt

COPY *.py .

CMD ["python", "leds.py"]
