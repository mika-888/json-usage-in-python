import requests

url = "https://jsonplaceholder.typicode.com/posts"

res = requests.get(url)

if res.status_code == 200:
    data = res.json()

    for post in data[:5]:
        print(post["id"], post["title"])
else:
    print("Error:", res.status_code)
