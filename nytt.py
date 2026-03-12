import requests, json


url = "http://192.168.20.35:8000/sitat"
text = input("skriv her:")
data = {
    "quote": text

}

response = requests.post(url, json=data)
data = response.json()
print(f"{data['message']} -ID:{data['id']}")
