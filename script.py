from dotenv import load_dotenv
import os
import requests
import json


# Load Key from env
load_dotenv()
api_key = os.getenv('API_KEY')
api_url = os.getenv('API_URL')

def download_catalog(url, collection_id):
    # Connection to Spotify API 
    r = requests.get(f"{url}/collections/{collection_id}/products.json",  headers={"X-Shopify-Access-Token": api_key})

    # Dict to JSON for creating the file.
    data = json.dumps(r.json(), indent=4)

    # Create the file once data has been converted to JSON obj
    with open('catalog.json', 'w') as output:
        output.write(data)

download_catalog(api_url, 198483837086)