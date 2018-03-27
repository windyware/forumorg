# forumorg

[![Website](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](https://www.forumorg.org)
![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/google/skia.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/15ea52785113c7b99f74/maintainability)](https://codeclimate.com/github/ForumOrganisation/forumorg/maintainability)

This is the repository of [Forum Organisation](https://www.forumorg.org)'s official website.

## Getting Started
These instructions will get help get your own copy of the project running on your local machine for development and testing purposes.

#### Install
First, you will need [Docker CE](https://docs.docker.com/install/) installed in your machine.

To check if it's been installed correctly, run `docker --version && docker-compose --version` and see if it returns something like this:

```sh
Docker version 17.09.0-ce, build afdb6d4
docker-compose version 1.16.1, build 6d1ac21
```

### Run
In order to run this project, checkout this github repository:
```sh
git clone https://github.com/ForumOrganisation/forumorg.git
```

And fill the following environment variables in a `.env` file at the root of the project:

```sh
BUCKET_NAME="bucket_name" # Required: S3 bucket name
SENDGRID_API_KEY="sendgrid_key" # Optional: for emailing events
RECAPTCHA_SECRET_KEY="recaptcha_key" # Optional: for recaptcha forms
```

To start the application, run `docker-compose up -d` and your app should be deployed at http://localhost:5000 !

If you want to access the terminal input/output of the application:

```sh
docker exec -ti $(docker ps | grep web | awk '{print $1}') sh
```

Note: for access to logs, run `docker-compose logs -f web`

You're now ready to write some code, your changes should be reflected in the application :) !

### Deploy

#### Heroku
The application is currently deployed on Heroku.

The Heroku Command Line Interface (CLI) makes it easy to create and manage your Heroku apps directly from the terminal.
It’s an essential part of using Heroku. Install it by following [these guidelines](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).

Heroku can be set to recognize your working app directory as the deployed heroku app(s), by adding the following git remotes:

```sh
git remote add production https://git.heroku.com/forumorg-prod.git
git remote add staging https://git.heroku.com/forumorg-staging.git
```

#### Deployment process
On ```any pull request``` ([see how](https://help.github.com/articles/creating-a-pull-request/)):
- A temporary review app is created, which can be live tested.
- If everything is working OK, the PR can be merged into `master`.

On ```push to master```:
- A build is triggered on our [staging app](https://forumorg-staging.herokuapp.com) (useful for testing in a production-like environment).

On ```heroku pipelines:promote -r staging --to production```:
- The staging app is instantly deployed to [production](https://www.forumorg.org).

## Running scripts
Some tasks on the platform requires one-off execution of scripts, like batch updates performed in database.

You can execute a script by adding it to **manage.py** as a python function, then run:

```sh
heroku local:run python manage.py my_script
```

## Localization
The app is localized using:

- Flask-Babel: used to indicate which strings needs to be translated (surrounded with `_('STRING')`)
- PhraseApp: provides a nice UI to translate the strings

You can get familiar with the process [by following this tutorial](https://phraseapp.com/blog/posts/python-localization-flask-applications/).

## Contributions

Contributions are very welcome! If you find a bug or some improvements, feel free to raise an issue and send a PR!

Please see the [CONTRIBUTING](CONTRIBUTING.md) file for more information on how to contribute.

## Authors

* **Mehdi BAHA** - [mehdibaha](https://github.com/mehdibaha)
* **Juliette BRICOUT** - [jbricout](https://github.com/jbricout)
* **Mohammed MEGZARI** - [momeg](https://github.com/momeg)
* **Hatim BINANI** - [TheHeisenberg](https://github.com/TheHeisenberg)
* **Ismail ZEMMOURI** - [IsmailZemmouri](https://github.com/IsmailZemmouri)
* **Ismail JATTIOUI** - [IsmailJattioui](https://github.com/yugismop)

(Note to contributors: Add yourself!)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
