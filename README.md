# forumorg

[![Website](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](https://www.forumorg.org)
![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/google/skia.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/15ea52785113c7b99f74/maintainability)](https://codeclimate.com/github/ForumOrganisation/forumorg/maintainability)

This is the repository of [Forum Organisation](https://www.forumorg.org)'s official website.

## Getting Started

These instructions will get help get your own copy of the project running on your local machine for development and testing purposes.

### Requirements

To get your development environment running, you need:

- [python 3](https://www.python.org/downloads/)
- [bower](https://bower.io/#install-bower)
- [mongodb](https://www.mongodb.com/download-center#community)

### Install

To install the necessary dependencies:

```sh
git clone https://github.com/ForumOrganisation/forumorg.git
cd forumorg && pip install -r requirements.txt
bower install
```

### Configuration
To start the project, you need to provide the following environment variables:

```sh
export MONGODB_URI="mongodb://host:port/dbname" # Required: local running mongodb instance
export BUCKET_NAME="bucket_name" # Required: S3 bucket name
export DEBUG=True # Optional: Nice for debugging
export SENDGRID_API_KEY="sendgrid_key" # Optional: for emailing events
```

### Run
```sh
python runserver.py
```

## Deploying
We use Heroku for Cloud hosting and Continuous Integration, using this continuous delivery workflow:

- A developer creates a pull request to make a change to the codebase.
- Heroku automatically creates a review app for the pull request, allowing developers to test the change.
- When the change is ready, it’s merged into the codebase’s master branch.
- The master branch is automatically deployed to [staging](https://forumorg-staging.herokuapp.com) for further testing.
- When it’s ready, the staging app is promoted to [production](https://www.forumorg.org), where the change is available to end users of the app.

## Localization
The app is localized using:

- Flask-Babel: used to indicate which strings needs to be translated (surrounded with `_('STRING')`)
- PhraseApp: provides a nice UI to translate the strings

You can get familiar with the process [by following this tutorial](https://phraseapp.com/blog/posts/python-localization-flask-applications/).

## Contributions

Contributions are very welcome! If you find a bug or some improvements, feel free to raise an issue and send a PR! Please see the [CONTRIBUTING](CONTRIBUTING.md) file for more information on how to contribute.

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
