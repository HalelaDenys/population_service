FROM python:3.11-slim

ENV PYTHONPATH=src

RUN apt-get update && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false && poetry install --no-root

COPY src/ /app/src/

CMD ["poetry", "run", "python", "src/get_data.py"]