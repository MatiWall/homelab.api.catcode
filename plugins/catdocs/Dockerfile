FROM docker-registry.mw.local/python:3.12-3

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

# Install Git
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

RUN poetry install --no-dev

COPY . /app

EXPOSE 8000

CMD ["poetry", "run", "python", "main.py"]
