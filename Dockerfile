FROM python:3.10-slim-buster

WORKDIR /usr/src/app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

RUN pip install pipenv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --system --deploy --ignore-pipfile

COPY . .

CMD ["flask", "run"]