import requests

url = "https://jsonplaceholder.typicode.com/users"

res = requests.get(url)

if res.status_code == 200:
    users = res.json()

    for user in users:
        print(user["name"], user["email"])
else:
    print("Error")
