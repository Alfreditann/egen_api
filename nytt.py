import reqyests

url = "http://192.168.20.35:8000/sitat"
data = {
    "quote": "test"

}

response = requests.post(url, json=data)
data = response.json()
print(f"{data["message"]} -ID:{data["id"]}")