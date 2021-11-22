from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
from pprint import pprint
import os

from service.db import Data_Base as db
from resources.funciones import *

'''
Importamos los datos del archivo
Si no existe, se crea y tiene que configurar
'''
try:
    from settings import DB, HOST, PORT
    print(f"Ajustes cargados:\n\tHOST: {HOST}\n\tDB: {DB}\n\tPORT: {PORT}")
except:
    settings = open("./settings.py", "w", encoding="utf-8")
    settings.write("DB = \"\"" + os.linesep)
    settings.write("HOST = \"\"" + os.linesep)
    settings.write("PORT = 5500" + os.linesep)
    settings.close()
    from settings import DB, HOST, PORT
    print(f"Ajustes cargados:\n\tHOST: {HOST}\n\tDB: {DB}\n\tPORT: {PORT}")

app = Flask(__name__)
CORS(app)

# GET
@app.route("/", methods=["GET"])
def ping():
    '''
    'Bienvenida
    '''
    return "Regalos API REST"

# POST
@app.route("/users/add", methods=["POST"])
def get_my_presets():
    data = request.get_json()
    pprint(data)

    if check_user_schema(data):
        if db.add_document(HOST, DB, "users", data.copy()):
            return jsonify(data)
    return jsonify({"error" : "Algo ha ido mal"})

@app.route("/users/add", methods=["POST"])
def new_user():
    data = request.get_json()
    pprint(data)

    if check_user_schema(data):
        if db.add_document(HOST, DB, "users", data.copy()):
            return jsonify(data)
    return jsonify({"error" : "Algo ha ido mal"})

@app.route("/presents/add", methods=["POST"])
def new_present():
    data = request.get_json()
    pprint(data)

    if check_present_schema(data):
        if db.add_document(HOST, DB, "presents", data):
            return jsonify(data)
    return jsonify({"error" : "Algo ha ido mal"})

@app.route("/items/add", methods=["POST"])
def new_item():
    data = request.get_json()
    pprint(data)

    if check_item_schema(data):
        if not db.get_data(HOST, DB, "presents", {"id" : data["id"]}):
            if db.add_document(HOST, DB, "presents", data):
                return jsonify(data)
    return jsonify({"error" : "Algo ha ido mal"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=PORT)