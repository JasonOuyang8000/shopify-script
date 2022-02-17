from dotenv import load_dotenv
import os


# Load Key from env
load_dotenv()
key = os.getenv('API_KEY')
