import os
from os.path import join, dirname
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

# タイムゾーンの生成
JST = timezone(timedelta(hours=+9), 'JST')

#データベースのURL周りの設定
load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ASYNC_DB_URL = os.environ.get("ASYNC_DB_URL")
DB_URL = os.environ.get("DB_URL")

print(ASYNC_DB_URL)
