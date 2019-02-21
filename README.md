# Ingredient Parser

Simple python parser for strings representing ingredients. The essential idea is that it compares the string, lazily, to a collection of regexes, returning the components of the string.

> "500.5 grams of salt" -> {'quantity': '500.5', unit: 'g', 'ingredient': 'salt'}

Input ingredient strings are assumed to be well formed, no input cleaning is done.
Strings that don't break down neatly along pattern lines are assumed to be ingredients and will return in the 'ingredient' field of the response (with a null in each of the other two fields).
Units are truncated to the first letter and lower cased. "GRAMS" -> "g".

> The following units are well-represented:
> t -> teaspoons
> c -> cups
> g -> grams
> Others might get a little strange, (ie. tbsp -> t AND tsp -> t).

>:hammer: Needs Improvement :hammer:
> Regexes assume that if there is a 3rd word, that the 2nd word is a 'unit'.
> ie. "2 jumbo eggs" -> {'quantity': '2', 'unit': 'j', 'ingredient': 'eggs'}
> Whatever a "j" is...

A minimal Flask app is included to expose the parsing function over HTTP.

> :bangbang: Flask server is *not production-ready* > :bangbang:

```bash
http --json  POST http://127.0.0.1:5000/parse-ingredient ing='500.5 grams of salt'

HTTP/1.0 200 OK
Content-Type: application/json
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
1. You may also want [httpie](https://httpie.org/) which will allow you to run the examples in this READ.me. You could use curl or postman if they're more your speed.

## Use

POST a request to `<host>:<port>/parse-ingredient` with json data keyed with `ing` to get back the response. Take a look at the httpie examples abvove and below for inspiration.

```bash
http --json  POST http://127.0.0.1:5000/parse-ingredient ing='salt and pepper to taste'

HTTP/1.0 200 OK
Content-Type: application/json
Server: Werkzeug/0.14.1 Python/3.7.2
{
    "ingredient": "salt and pepper to taste",
    "quantity": null,
    "unit": null
}
```

## Testing

Run `pipenv run pytest` to execute the pytest tests.