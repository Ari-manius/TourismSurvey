FROM python:3.12-alpine
USER root
RUN apk update && apk upgrade
RUN apk add build-base git postgresql-dev
RUN pip install virtualenv
RUN mkdir /app
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN virtualenv env -p python
ENV PATH="/app/env/bin:$PATH"
RUN pip install -r requirements.txt
RUN apk del build-base
COPY ./ /app/
CMD ["otree", "prodserver", "8000"]


# docker compose build --no-cache otree
# docker compose up -d
