FROM python:alpine

# Installing packages
RUN apk update \
    && apk add --no-cache --virtual .build_deps \
    # Enable c-based pip dependencies
    build-base python3-dev libffi-dev \
    # Enable Pillow pip dependency
    zlib-dev jpeg-dev \
    # Install npm
    nodejs \
    # Install git
    git

RUN npm install -g bower

WORKDIR /app

# Install pip dependencies
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install bower & dependencies
COPY ./bower.json .
COPY ./.bowerrc .
RUN bower install --allow-root --config.interactive=false -f bower.json

# Copy source code
COPY . ./

# Run application
CMD ["gunicorn", "app:app"]
