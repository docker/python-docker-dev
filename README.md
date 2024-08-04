# python-docker-dev

A simple Python app for Docker's Python Language Guide.

## Setup

1. Build and start the containers:
    ```sh
    docker-compose up --build
    ```

2. Access the application at [http://localhost:5000](http://localhost:5000).

## Endpoints

- `/`: Returns a welcome message.
- `/widgets`: Fetches widgets from the database.
- `/initdb`: Initializes the database.

A simple Python app for [Docker's Python Language Guide](https://docs.docker.com/language/python).
