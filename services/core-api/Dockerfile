# Stage 1: Build stage
FROM docker-registry.mw.local/python:3.12-2 AS builder

# Set the working directory in the container
WORKDIR /app

# Copy only the dependencies definition files
COPY pyproject.toml poetry.lock /app/

# Install Poetry
RUN poetry install --no-dev

# Stage 2: Final image
FROM docker-registry.mw.local/python:3.12-2

# Set the working directory in the container
WORKDIR /app

# Copy the application code from the builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY . .

# Make port 8080 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "main.py"]
