FROM python:3.9-slim
WORKDIR /app/url-shortener
COPY ./pyproject.toml /app/url-shortener/pyproject.toml
COPY ./poetry.lock /app/url-shortener/poetry.lock
COPY ./app /app/url-shortener/app
RUN apt-get update && apt-get install curl -y
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"
RUN poetry install
EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]