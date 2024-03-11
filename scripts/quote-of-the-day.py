import os
import requests
import json

API_KEY = os.environ.get("API_KEY_NINJA_API");

category = 'success'
api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
# Expand the ~ character to represent the user's home directory
file_path = os.path.expanduser("~/quote.txt")

with open(file_path, "w") as file:
    if response.status_code == requests.codes.ok:
        data = json.loads(response.text)
        file.write(data[0]['quote'])
    else:
        print("Error:", response.status_code, response.text)

