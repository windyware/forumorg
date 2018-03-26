FROM python:alpine

ARG PORT
ARG MONGODB_URI
ARG DEBUG

ENV APP_DIR=/app
ENV INTL_DIR=./app/static/bower_components/intl-tel-input/build/img

WORKDIR $APP_DIR

# Installing packages
RUN apk update \
    && apk add --no-cache --virtual .build_deps \
    # Enable c-based pip dependencies
    build-base python3-dev libffi-dev \
    # Enable Pillow pip dependency
    zlib-dev jpeg-dev \
    # Enable npm
    nodejs \
    # Enable git
    git

RUN npm install -g bower

# Install bower & dependencies
COPY ./bower.json .
RUN bower install --allow-root --config.interactive=false -f bower.json

# Install pip dependencies
COPY ./requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Copy & build assets
COPY $INTL_DIR $APP_DIR/$INTL_DIR
RUN python manage.py assets build

# Cleaning up everything
RUN apk del .build_deps && rm -rf /var/cache/apk/*

CMD ["gunicorn", "app:app"]
