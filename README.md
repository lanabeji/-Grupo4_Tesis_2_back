# Grupo 4 - Tesis 2 - Backend

## Requirements

- Python 3.10.6
- Postgresql

## Database

You should specify DB_HOST, DB_PORT, DB_USER and DB_PASSWORD or the server is going to use the following default values.

- DB_HOST -> localhost
- DB_PORT -> 5432
- DB_USER -> postgres
- DB_PASSWORD -> postgres
- DB_NAME -> dermoapp for development and dermoapp_test for unit tests

## Install dependencies

```bash
pip install -r ./requirements.txt
```

## Run server

```bash
FLASK_APP=./src/main.py flask run -h 0.0.0.0 --port=8080
```

## Run tests

```bash
pytest --cov=src -v -s --cov-fail-under=80
```