import requests

url="https://jsonplaceholder.typicode.com/posts/1"

data={
    "title":"Updated Title"
}

response=requests.put(
    url,
    json=data
)

print(response.status_code)