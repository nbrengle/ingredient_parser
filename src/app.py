"""Minimal Flask Api."""
from flask import Flask, jsonify, request

from ingredient_parser import parse_ingredient

api = Flask(__name__)


@api.route("/parse-ingredient", methods=["POST"])
def ingredient():
    """Extract the request json, hand it off to parser, jsonify response."""
    ingredient = request.get_json().get("ing")
    return jsonify(parse_ingredient(ingredient))


if __name__ == "__main__":
    api.run(host="0.0.0.0", debug=True)
