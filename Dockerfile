FROM python:alpine

ENV APP_DIR=/app

WORKDIR $APP_DIR

# Installing packages
RUN apk update \
    && apk add --no-cache --virtual .build_deps build-base python3-dev libffi-dev \
    && apk add --no-cache nodejs \
                          git \
                          zlib-dev jpeg-dev

RUN npm install -g bower

# Install bower & dependencies
COPY ./bower.json .
RUN bower install --allow-root --config.interactive=false -f bower.json

# Install pip dependencies
COPY ./requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt
RUN python manage.py assets build

# Cleaning up everything
RUN apk del .build_deps && rm -rf /var/cache/apk/*

CMD ["gunicorn", "app:app"]