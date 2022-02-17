from dotenv import load_dotenv
import os
import requests



# Load Key from env
load_dotenv()
key = os.getenv('API_KEY')
url = os.getenv('URL')

# Connection to Spotify API Database
r = requests.post('https://xgentest.myshopify.com/admin/api/2022-01/graphql.json', auth=('user', 'pass'))
