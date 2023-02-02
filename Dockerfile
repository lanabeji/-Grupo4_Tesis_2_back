FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && \
  apt-get install -y libpq-dev gcc && \
  apt-get install -y --no-install-recommends gcc python3-dev libssl-dev

RUN pip install pipenv psycopg2

COPY . .

RUN pip install -r ./requirements.txt

EXPOSE 8080

ENV FLASK_APP="./src/main.py"

ENTRYPOINT ["flask", "run", "-h", "0.0.0.0", "--port=8080"]
