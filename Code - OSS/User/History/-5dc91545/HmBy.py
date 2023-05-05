import os

# needed for getting .env file
from dotenv import load_dotenv
load_dotenv()

# Getting API Keys from .env file and assigning them to a variable
API_KEY_WALLHEAVEN = os.environ.get("API_KEY_WALLHEAVEN")









# print(API_KEY_WALLHEAVEN)