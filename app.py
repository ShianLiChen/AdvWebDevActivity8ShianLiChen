# app.py
from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")


@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json(force=True)
    return jsonify(data), 201


@app.route('/update', methods=['PUT'])
def update():
    data = request.get_json(force=True)
    updated_data = {"updated": True, **data}
    return jsonify(updated_data), 200


@app.route('/remove', methods=['DELETE'])
def remove():
    data = request.get_json(force=True)
    deleted_data = {"deleted": True, **data}
    return jsonify(deleted_data), 200


if __name__ == '__main__':
    app.run(debug=True)
