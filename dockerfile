FROM python:3.10-slim-buster as build
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
build-essential gcc 

RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

COPY ./api/requirements.txt /app/venv
RUN pip3 install -r /app/venv/requirements.txt

COPY ./api/ /app/venv


#Using a small base image to reduce attack area, as well as pinning the image digest
FROM python:3.10-slim-buster@sha256:a2e9d4e5340453ec31ef0a7e5fb928b3f224387c2f75e9834f83187d2395f83c

RUN groupadd -g 999 python && \
    useradd -r -u 999 -g python python

WORKDIR /app/venv
COPY --chown=python:python --from=build /app/venv /app/venv


USER 999

ENV PATH="/app/venv/bin:$PATH"
CMD ["python3", "apiRoutes.py"]






