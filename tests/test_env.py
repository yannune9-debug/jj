import os
from dotenv import load_dotenv

print("CWD:", os.getcwd())  # where Python thinks it's running from

load_dotenv()

print("BASE_URL:", os.getenv("BASE_URL"))
