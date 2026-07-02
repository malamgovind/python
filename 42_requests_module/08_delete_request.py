import requests

url="https://jsonplaceholder.typicode.com/posts/1"

response=requests.delete(url)

print(response.status_code)