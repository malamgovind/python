import json

data = {
    "name":"Govind",
    "age":22
}

print(
    json.dumps(
        data,
        indent=4
    )
)
# index = 4 : દરેક nested level માટે 4 spaces આપીને JSON ને સુંદર (pretty print) બનાવવું.