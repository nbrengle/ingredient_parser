# Ingredient Parser

Simple python parser for strings representing ingredients. The essential idea is that it compares the string, lazily, to a collection of regexes, returning the components of the string.

> "500.5 grams of salt" -> {'quantity': '500.5', unit: 'g', 'ingredient': 'salt'}

A minimal Flask app is included to expose the parsing function over HTTP.
