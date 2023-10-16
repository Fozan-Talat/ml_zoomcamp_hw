import requests
url = "http://localhost:9696/q4_predict"
client = {"job": "unknown", "duration": 270, "poutcome": "failure"}
response=requests.post(url, json=client).json()

print(response)