import os
from os.path import join, dirname
from dotenv import load_dotenv


load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ASYNC_DB_URL = os.environ.get("ASYNC_DB_URL")
DB_URL = os.environ.get("DB_URL")

print(ASYNC_DB_URL)
