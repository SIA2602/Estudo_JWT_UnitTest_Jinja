from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import json
import jwt
from datetime import datetime

aplication = Flask(__name__)
CORS(aplication)
apiRestFull = Api(aplication)

key = "secret"
hashToken = jwt.encode({"user": "sia2602", "password": "Ola_mundo!" }, key, algorithm="HS256")

users = [
    {
      "user": "sia26",
      "password": hashToken
    },
    {
      "user": "sia260",
      "password": hashToken
    },
    {
      "user": "sia2602",
      "password": hashToken
    }
]

#Funcao que permite POST ou GET para as unidades
class autorization(Resource):  
  def post(self):
    print(request.headers.get('Chave'))
    data = json.loads(request.data) 
    print(data)    
    for i in range(len(users)):      
      if(users[i]["password"] == jwt.encode(data, key, algorithm="HS256")):
        return({"status_code": 200,
        "items":{
          "access_token": jwt.encode({"user": "sia2602", "exp": datetime.now()}, key, algorithm="HS256")
        }})      
    return {
      'status_code': 404,
      'error': 'Failed to connect',
      'description': 'Could not access information'
    }

apiRestFull.add_resource(autorization, "/auth")

if __name__ == "__main__":
    aplication.run(debug=True)