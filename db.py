import os
import pymysql
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    connection = pymysql.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "registration"),
        port=int(os.getenv("DB_PORT", "3306"))
    )

    return connection