import os
from dotenv import load_dotenv
load_dotenv()

API_KEY_WALLHEAVEN = os.environ.get(wall)
print(API_KEY_WALLHEAVEN)