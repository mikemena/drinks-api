# drinks

# Usage of Docker

1 - Define Dockerfile : Contains all the operating sysem level dependencies that the project needs

2 - Create Docker Compose configuration : Tells Docker how to run the images that are created from the Docker file configuration

3 - Run all commands via Docker Compose

# Set up Docker & Github

1 - Once the github project is set up, go to Docker Hub website > Settings > Security to generate a security token. This token will be used in the project when it needs to connect to docker to do things. that way we do not have to use our creds....
https://hub.docker.com/settings/security

Generate token and keep the dialog open once it generates it
2 - Go to github project > settings > secrets and variables > codespaces < New repository secret button. Add two secrets:

DOCKERHUB_USER - set to docker username
DOCKERHUB_TOKEN - set to docker token

# Docker & Django

1- Create a Dockerfile
2- List steps for creating image
a- Choose a base image (python)
b- Install dependencies
c- Setup users
3- Set up docker compose
a- Name (eg:app)
b- Port mapping
c- Volume mappings

# Using Docker Compose

```
docker-compose run --rm app sh -c "python manage.py collectstatic

```

explanation:

docker-compose - runs a Docker Compose command
run - will start a specific container defined in config
--rm - removes the container after its completed
app - the name of the service
sc -c - passes in a shell command
the rest inside quotations is the django command to run inside the container

# Build an image

- Go to terminal. Make sure you are at the app directory:

```
docker build .

```

- Build compose

```
docker-compose build

```

# Create Django project

```
docker-compose run --rm app sh -c "django-admin startproject app ."

```

# Run development server

To start the server locally at http://127.0.0.1:8000/:

```
docker-compose up

```
