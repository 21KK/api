import requests

payload = {
    "username": "ray21",
    "email": "ray@orazen.com",
    "password": "securedenvironment"}

headers = {
    "Content-Type": "application/json"}

response = requests.post("http://localhost:8000/register", json=payload, headers=headers)
print("Status Code:", response.status_code)
print("Response Body:", response.json())