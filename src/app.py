from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/parse-ingredient', methods=["POST"])
def parse_ingredient():
    ingredient = request.args.get('ing')
    return jsonify(parse_ingredient(ingredient))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)