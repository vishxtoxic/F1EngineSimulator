FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml README.md ./
COPY src ./src

RUN pip install -e ".[dev]" \
    && useradd --create-home appuser \
    && chown -R appuser:appuser /app

USER appuser

CMD ["pytest"]
