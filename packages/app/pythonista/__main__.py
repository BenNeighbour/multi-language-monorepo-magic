import requests

# URL for the request
url = "https://jsonplaceholder.typicode.com/posts/1"

# Make a GET request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the response as JSON
    data = response.json()
    print("Response Data:", data)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
