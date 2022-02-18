from dotenv import load_dotenv
import os
import requests
import json


# Load Key from env
load_dotenv()
key = os.getenv('API_KEY')
url = os.getenv('API_URL')


# Connection to Spotify API 
r = requests.get(f"{url}/collections/198483837086/products.json",  headers={"X-Shopify-Access-Token": key})

# Dict to JSON for creating the file.
data = json.dumps(r.json(), indent=4)

# Create the file once data has been converted to JSON obj
with open('catalog.json', 'w') as output:
    output.write(data)