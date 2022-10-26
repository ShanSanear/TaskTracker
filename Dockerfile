FROM python:3.10.8
WORKDIR /code
ENV PYTHONPATH "${PYTHONPATH}:/code/src"
RUN curl -sSL https://install.python-poetry.org | python3 -

COPY poetry.lock /code/
COPY pyproject.toml /code/

RUN /root/.local/bin/poetry update
RUN /root/.local/bin/poetry install


COPY src/api /code/api
