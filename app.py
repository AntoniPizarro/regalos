from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
from pprint import pprint

from service.db import Data_Base as db
from resources.funciones import *

DB = "regalos"
HOST = "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.4uubd.mongodb.net/" + DB + "?retryWrites=true&w=majority"
PORT = 5505

app = Flask(__name__)
CORS(app)

# GET
@app.route("/", methods=["GET"])
def ping():
    '''
    'Bienvenida
    '''
    return "Regalos API REST"

@app.route("/users/add", methods=["POST"])
def new_user():
    data = request.get_json()
    pprint(data)

    if check_user_schema(data):
        db.add_document(HOST, DB, "users", data)
    return jsonify(data)

@app.route("/presents/add", methods=["POST"])
def new_present():
    data = request.get_json()
    pprint(data)

    if check_present_schema(data):
        db.add_document(HOST, DB, "presents", data)
    return jsonify(data)

@app.route("/items/add", methods=["POST"])
def new_item():
    data = request.get_json()
    pprint(data)

    if check_item_schema(data):
        if not db.get_data(HOST, DB, "presents", {"id" : data["id"]}):
            db.add_document(HOST, DB, "presents", data)
            return jsonify(data)
    return jsonify({"error" : "Algo ha ido mal"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=PORT)