import requests

try:

    response=requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        timeout=2
    )

    print(response.status_code)

except requests.exceptions.Timeout:

    print("Request Timed Out")