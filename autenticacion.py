import json
import jwt
from flask import Flask, request
from controlDados import retornarTiros as tiro
app = Flask(__name__)


public_key = b'''-----BEGIN PUBLIC KEY-----\n
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnzyis1ZjfNB0bBgKFMSv
vkTtwlvBsaJq7S5wA+kzeVOVpVWwkWdVha4s38XM/pa/yr47av7+z3VTmvDRyAHc
aT92whREFpLv9cj5lTeJSibyr/Mrm/YtjCZVWgaOYIhwrXwKLqPr/11inWsAkfIy
tvHWTxZYEcXLgAXFuUuaS3uF9gEiNQwzGTU1v0FqkqTBr4B8nW3HCN47XUu0t8Y0
e+lf4s4OxQawWD79J9/5d3Ry0vbV3Am1FtGJiJvOwRsIfVChDpYStTcHTCMqtvWb
V6L11BWkpzGXSW4Hv43qa+GSYOD2QU68Mb59oSk2OB+BtOLpJofmbGEGgvmwyCI9
MwIDAQAB
-----END PUBLIC KEY-----'''


def token_required(something):
    def wrap(cantidad):
        try:
            token_passed = request.headers['Authorization'].split(" ")[1]
            if request.headers['Authorization'] != '' and request.headers['Authorization'] != None:
                try:
                    jwt.decode(token_passed, public_key, algorithms='RS256')
                    tiros = tiro(cantidad)
                    data = {'dados': tiros}
                    return app.response_class(response=json.dumps(dict(data)), mimetype='application/json'), 200
                except jwt.exceptions.ExpiredSignatureError:
                    return_data = {
                        "error": "1",
                        "message": "Token has expired"
                    }
                    return app.response_class(response=json.dumps(return_data), mimetype='application/json'), 401
                except:
                    return_data = {
                        "error": "1",
                        "message": "Invalid Token"
                    }
                    return app.response_class(response=json.dumps(return_data), mimetype='application/json'), 401
            else:
                return_data = {
                    "error": "2",
                    "message": "Token required",
                }
                return app.response_class(response=json.dumps(return_data), mimetype='application/json'), 401
        except Exception as e:
            return_data = {
                "error": "3",
                "message": str(e)
            }
            return app.response_class(response=json.dumps(return_data), mimetype='application/json'), 500

    return wrap
