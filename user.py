import requests

request = requests.post("http://127.0.0.1:5000/auth", json={"user": "sia2602","password": "Ola_mundo!"})
print(request.json())

request = requests.post("http://127.0.0.1:5000/auth", headers={"Chave": "hal"}, json={"user": "sia2602","password": "Ola_mundo!"})
print(request.json())

