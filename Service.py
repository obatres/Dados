from flask import Flask, request, json, Response
from random import randint as ran
import json
from autenticacion import token_required
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/tirar/<int:cantidad>', methods=['GET'])
@token_required
def index(cantidad):
    res = {'Token': "autorizado"}
    return Response(response=json.dumps(res),
                    mimetype='application/json')


@app.route('/token', methods=['GET'])
def token_auth():
    res = {'Token': "autorizado"}
    return Response(response=json.dumps(res),
                    mimetype='application/json')


if __name__ == '__main__':

    app.run(debug=True, port=5002, host='0.0.0.0')
