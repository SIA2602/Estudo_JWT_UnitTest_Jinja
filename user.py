import requests

print(requests.post("http://127.0.0.1:5000/validate", json={"user": "sia2602","password": "Ola_mundo!"}).text)

