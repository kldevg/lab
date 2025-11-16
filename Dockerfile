FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY src/lab .

RUN pip install poetry && poetry install --no-root --no-interaction

EXPOSE 5000
CMD ["poetry", "run", "python", "appli.py"]