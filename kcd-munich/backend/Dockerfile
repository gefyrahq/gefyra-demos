FROM python:3.9-slim

RUN pip install poetry

RUN mkdir /app
WORKDIR /app
COPY pyproject.toml /app/

RUN poetry install

COPY app.py /app/
EXPOSE 5002

CMD ["poetry", "run", "flask",  "--app", "app", "--debug", "run", "--port", "5002", "--host", "0.0.0.0"]
