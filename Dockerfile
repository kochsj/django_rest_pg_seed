FROM python:3.7-slim

# Environment Variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

COPY Pipfile .
COPY Pipfile.lock .

# Install dependencies
RUN pip install pipenv && pipenv install --system

COPY . /code
