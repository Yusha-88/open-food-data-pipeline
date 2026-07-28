FROM python:3.13.14
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /code

COPY pyproject.toml .python-version uv.lock ./
RUN uv sync --locked

# WORKDIR /code
# COPY pipeline.py .