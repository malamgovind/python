import requests

headers = {
    "User-Agent":"Python"
}

response = requests.get(
    "https://httpbin.org/headers",
    headers=headers
)

print(response.status_code)
print(response.text)