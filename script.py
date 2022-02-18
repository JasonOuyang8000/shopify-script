from dotenv import load_dotenv
import os
import requests
import json




# Load Key from env
load_dotenv()
key = os.getenv('API_KEY')
url = os.getenv('API_URL')


# Connection to Spotify API Database
r = requests.get(f"{url}/collections/198483837086/products.json",  headers={"X-Shopify-Access-Token": key})
data = json.dumps(r.json(), indent=4)
print(type(data))

with open('catalog.json', 'w') as output:
    output.write(data)