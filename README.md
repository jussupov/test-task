# Quick Start Guide 🚀

## Prerequisites

Ensure you have the following installed on your system:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Poetry](https://python-poetry.org/docs/)

## Installation

### 1. Clone the Repository

```sh
git clone https://github.com/jussupov/test-task
cd test-task
```

### 2. Create and Configure Environment Variables

Copy the example environment file and fill in the required values:

```sh
cp .env.example .env
```

Edit `.env` and set the necessary environment variables:

```ini
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=*
POSTGRES_DB=b2broker_db
POSTGRES_USER=jussupov
POSTGRES_PASSWORD=strongpassword
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

### 3. Build and Start the Project

Run the following command to build and start the application:

```sh
docker-compose up --build
```

This will:

- Pull the PostgreSQL image
- Build the Django application
- Start both services

### 4. Apply Migrations and Create a Superuser

After the containers are running, apply the migrations:

```sh
docker-compose exec web poetry run python manage.py makemigrations
docker-compose exec web poetry run python manage.py migrate
```


### 5. Access the Application

- **API/Website:** [http://localhost:8000/](http://localhost:8000/)


## Development Workflow

### Stop the Containers

```sh
docker-compose down
```

### Restart the Containers

```sh
docker-compose up -d
```

### Check Logs

```sh
docker-compose logs -f web
```

### Run Tests

```sh
docker-compose exec web poetry run python manage.py test
```

## Notes

- **Pre-commit hooks** are used for linting and formatting; install them with:
  ```sh
  pre-commit install
  ```
---



