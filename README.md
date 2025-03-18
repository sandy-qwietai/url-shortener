# url-shortener

# This application contains the following API endpoints

1. POST /url/shorten
2. GET /:short_url
3. GET /url/metrics

# Steps to run the application on local

Run the below command to install poetry 

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Run the below command inside the url-shortener directory to install all the dependencies present in poetry.lock file

```bash
poetry install
```

Run the below command inside the url-shortener directory to run the unit tests

```bash
poetry run pytest
```

Run the below command inside the url-shortener directory to start the backend server

```bash
poetry run uvicorn app.main:app
```

Go to http://localhost:8000/docs for accessing the swagger docs of the backend server


# Steps to run the application on docker container

Run the below command inside the url-shortener directory to build the docker image of backend server

```bash
docker build -t url-shortener .
```

Run the below command to run docker container

```bash
docker run -p 8000:8000 url_shortener
```

Go to http://localhost:8000/docs for accessing the swagger docs of the backend 

# Docker image for this application is present at the below link to docker hub

https://hub.docker.com/repository/docker/sandeepkrjha123/url-shortener/general