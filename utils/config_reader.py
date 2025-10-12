# utils/config_reader.py
import os
from dotenv import load_dotenv

# load .env at import time
load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL")
    # EMAIL = os.getenv("EMAIL")
    # PASSWORD = os.getenv("PASSWORD")
