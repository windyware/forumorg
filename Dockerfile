FROM python:alpine

# Setting environement variables from docker-compose
ARG PORT
ARG MONGODB_URI
ARG DEBUG

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

WORKDIR /app

# Install pip dependencies
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install bower & dependencies
COPY . $APP_DIR
RUN bower install --allow-root --config.interactive=false -f bower.json

# Build assets
RUN python manage.py assets build

CMD ["gunicorn", "app:app"]
