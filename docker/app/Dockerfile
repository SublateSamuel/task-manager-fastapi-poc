FROM python:3.11
RUN apt-get update && \
    apt-get install -y --no-install-recommends
WORKDIR /app
COPY pyproject.toml /app/
ENV POETRY_HOME="/opt/poetry" \
    POETRY_VERSION=1.4.2
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --verbose --no-ansi
EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
#ENTRYPOINT ["tail", "-f", "/dev/null"]