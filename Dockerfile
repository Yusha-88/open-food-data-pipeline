FROM python:3.13.14
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"

COPY "pyproject.toml" ".python-version" "uv.lock" ./
RUN uv sync --locked

# WORKDIR /code
COPY pipeline.py .

# Set entry point to run ETL script
ENTRYPOINT ["python", "pipeline.py"]