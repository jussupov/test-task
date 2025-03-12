# use python image
FROM python:3.11

# set working dir
WORKDIR /app

# Install dependencies
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --no-root

# Copy code of project
COPY . .

# Open port 8000
EXPOSE 8000

# Run server
CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8000", "b2broker.wsgi:application"]

