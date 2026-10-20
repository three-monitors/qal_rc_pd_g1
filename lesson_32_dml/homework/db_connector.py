import psycopg
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()


def get_connection():
    dsn = os.getenv("DATABASE_URL")
    return psycopg.connect(dsn)
