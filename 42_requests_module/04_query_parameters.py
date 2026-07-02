import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId":1
}

response = requests.get(
    url,
    params=params
)

print(response.url)