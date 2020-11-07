import json
import jwt
from flask import Flask, request
from controlDados import retornarTiros as tiro
from datetime import datetime
app = Flask(__name__)


public_key = b'''-----BEGIN PUBLIC KEY-----\n
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAoG1AtgVgbMpWjlGR3P5x
cJZIKtuDmQW15gdc/mHb6K4EGwupegg+IXu5XiKDcLfWuwK39Fx2XBE/H/Al8l3W
iEPlSH1aeATnaY4LaP2mg3sn21R3Eps1Z3j234HJIAk3vModg71yHhp11ieqHcXx
eECcAll7Qwo62lFYyPdZliAH3pBZzSV3V5JN54yWT4BU8qouCgcGsEstp7h2J0mK
qZ7tHZUji5BKdlNzLtNUQkvqgLY5earSVesx8RN7sixXUfRj7Rc84IM445Rhj8IT
Bt0rb8Lyn+JJxIYeBmuqwbMM/DJGVT3jsD9PGiSKgrpvPuKCG7kNEuZ/yPtJ+NsJ
Lh78zC7GNbvBauMjFYRmtXE+3OjU3yGEZwaPVauOBtgfX3manLsXw/FVxBN3E5CZ
hHJhAEbjVYXnkRp6I8kswxf/4B0asMA1/mlqQAJXcuZRXLO4st8MNsf5h7wHLwhe
9oR/dP2dpaOLMl4q3QXFVH1JLS7IFFQJIasaqy3zJcruxE73UcK4L8dHUPdfeTZA
MMFJ2U4Ep663c1l25DVWFwlPjaRogcMaKWLsHoG+FBvd8zYdr27IprKY61vCT83l
XJipA89Jq4FB4Nc6RUrj6ZVDyMV8Vp4tIHk+x9BcBQh+judMJSc/avCA8z0qW4Ou
ZVvHLLcL5kVSLIGpgq5AwbcCAwEAAQ==
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
