# Ingredient Parser

Simple python parser for strings representing ingredients. The essential idea is that it compares the string, lazily, to a collection of regexes, returning the components of the string.

> "500.5 grams of salt" -> {'quantity': '500.5', unit: 'g', 'ingredient': 'salt'}

A minimal Flask app is included to expose the parsing function over HTTP.

```bash
http --json  POST http://127.0.0.1:5000/parse-ingredient ing='500.5 grams of salt'
HTTP/1.0 200 OK
Content-Length: 67
Content-Type: application/json
Date: Thu, 21 Feb 2019 07:05:28 GMT
Server: Werkzeug/0.14.1 Python/3.7.2
{
    "ingredient": "salt",
    "quantity": "500.5",
    "unit": "g"
}
```

## Installation

1. if you don't already have: [docker](https://docs.docker.com/install/), [python 3.7](https://www.python.org/downloads/release/python-370/), [pipenv](https://pipenv.readthedocs.io/en/latest/), [docker-compose](https://docs.docker.com/compose/install/) and [git](https://git-scm.com/) you will need to install them.
If you're working on MacOS, [homebrew](https://brew.sh/) will be your best friend if you don't already have those dependencies.
1. clone the repo, navigate to it
1. run `pipenv install` to fetch the project's dependencies
1. or, once your docker daemon is running, `docker-compose build` -> `docker-compose up` and the image will install the dependencies.
1. You may also want [httpie](https://httpie.org/) which will allow you to run the example above. You could use curl or postman.

## Use

POST a request to host:port/parse-ingredient with json data keyed with `ing` to get back the response. Take a look at the example above for inspiration.

## Testing

Run `pipenv run pytest` to execute the pytest tests.