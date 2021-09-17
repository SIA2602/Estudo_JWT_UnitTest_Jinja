from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import json
import jwt

aplication = Flask(__name__)
CORS(aplication)
apiRestFull = Api(aplication)

key = "secret"
hashToken = jwt.encode({"user": "sia2602", "password": "Ola_mundo!" }, key, algorithm="HS256")

users = [
    {
      "user": "sia2602",
      "password": hashToken
    }
]

#Funcao que permite POST ou GET para as unidades
class validate(Resource):  
  def post(self):
    data = json.loads(request.data)     
    for i in range(len(users)):
      print(users[i])
      if(users[i]["password"] == jwt.encode(data, key, algorithm="HS256")):
        return({"status_code": 200})      
    return {
      'status_code': 404,
      'error': 'Failed to connect',
      'description': 'Could not access information'
    }

apiRestFull.add_resource(validate, "/validate")

if __name__ == "__main__":
    aplication.run(debug=True)