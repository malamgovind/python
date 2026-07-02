import requests

print("Before Request")

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1",
    timeout=10,
)

print("After Request")
print(response.status_code)
print(response.text)