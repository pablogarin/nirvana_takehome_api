FROM python:3.8-slim-buster

WORKDIR /app

COPY . ./

RUN python -m pip install -r requirements.txt

CMD ["gunicorn", "-w1", "-b0.0.0.0:5000", "--timeout", "30", "wsgi:app"]