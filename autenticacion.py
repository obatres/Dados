import json
import jwt
from flask import Flask, request
from controlDados import retornarTiros as tiro
from datetime import datetime
app = Flask(__name__)


public_key = b'''-----BEGIN PUBLIC KEY-----\n
MIGeMA0GCSqGSIb3DQEBAQUAA4GMADCBiAKBgFUEX63ip/USZRCw1DduN+Auda5J
kces0n61Ct4LkRe89peS8m4tGQluRG8A5giFgf+vYFpUMP+kiob7shCe+d6oN3Xd
/QSIeghpfby4W/v3wyl4oeAKkutYeOK9cRS0VEWzzOtGVvFhqwL4NJdSCAmff7+g
H5Hi9PHiT5hC/jVtAgMBAAE=
-----END PUBLIC KEY-----'''

Log = open("LogDados.txt", "a")


def token_required(something):
    def wrap(cantidad):
        try:
            token_passed = request.headers['Authorization'].split(" ")[1]
            if request.headers['Authorization'] != '' and request.headers['Authorization'] != None:
                try:
                    jwt.decode(token_passed, public_key, algorithms='RS256')
                    tiros = tiro(cantidad)
                    data = {'dados': tiros}
                    now = datetime.now()
                    print(str(now)+str(data), "COD: 200;")
                    Log.write(str(now)+" "+str(data) + "COD: 200;"+"\n")
                    Log.close()
                    return app.response_class(response=json.dumps(dict(data)), mimetype='application/json'), 200
                except jwt.exceptions.ExpiredSignatureError:
                    return_data = {
                        "error": "1",
                        "message": "Token has expired"
                    }
                    now = datetime.now()
                    print(str(now)+str(return_data), "COD: 400;")
                    Log.write(str(now)+" "+str(return_data) + "COD: 400;"+"\n")
                    Log.close()
                    return app.response_class(response=json.dumps(return_data), mimetype='application/json'), 400
                except:
                    return_data = {
                        "error": "1",
                        "message": "Invalid Token"
                    }
                    now = datetime.now()
                    print(str(now)+str(return_data), "COD: 400;")
                    Log.write(str(now)+" "+str(return_data) + "COD: 400;"+"\n")
                    Log.close()
                    return app.response_class(response=json.dumps(return_data), mimetype='application/json'), 400
            else:
                return_data = {
                    "error": "2",
                    "message": "Token required",
                }
                now = datetime.now()
                print(str(now)+str(return_data), "COD: 400;")
                Log.write(str(now)+" "+str(return_data) + "COD: 400;"+"\n")
                Log.close()
                return app.response_class(response=json.dumps(return_data), mimetype='application/json'), 400
        except Exception as e:
            return_data = {
                "error": "3",
                "message": str(e)
            }
            now = datetime.now()
            print(str(now)+str(return_data), "COD: 500;")
            Log.write(str(now)+" "+str(return_data) + "COD: 500;"+"\n")
            Log.close()
            return app.response_class(response=json.dumps(return_data), mimetype='application/json'), 500

    return wrap
