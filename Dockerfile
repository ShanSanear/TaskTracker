FROM python:3.10.8
WORKDIR /code

COPY poetry.lock /code/
COPY pyproject.toml /code/
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN /root/.local/bin/poetry update
RUN /root/.local/bin/poetry install

ENV PYTHONPATH "${PYTHONPATH}:/code/src"
RUN echo $PYTHONPATH
COPY src/api /code/api