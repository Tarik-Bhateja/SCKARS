import requests

# Replace this URL with the URL of the dummy API you want to fetch data from
url = 'https://jsonplaceholder.typicode.com/posts'

# Sending a GET request to the API
response = requests.get(url)

# Checking if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()  # Parsing the response JSON data
    for item in data:
        print(item)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
