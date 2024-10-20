import requests
from jsonschema import validate, ValidationError

# URL for the request
url = "https://jsonplaceholder.typicode.com/posts/1"

# Define the expected schema for the JSON response
schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    },
    "required": ["userId", "id", "title", "body"]
}

# Make a GET request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the response as JSON
    data = response.json()
    print("Response Data:", data)

    # Validate the JSON data against the schema
    try:
        validate(instance=data, schema=schema)
        print("JSON data is valid.")
    except ValidationError as e:
        print(f"JSON data is invalid: {e.message}")

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
