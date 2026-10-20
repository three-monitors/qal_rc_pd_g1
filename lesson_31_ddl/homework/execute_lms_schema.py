import psycopg
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
DSN = os.getenv("DATABASE_URL")


def execute_sql_file(filename):
    script_dir = Path(__file__).parent
    file_path = script_dir / filename

    with open(file_path, 'r', encoding='utf-8') as f:
        sql = f.read()

    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            conn.commit()
    print(f"Виконано: {filename}")


if __name__ == "__main__":
    execute_sql_file("lms_schema.sql")
    print("Таблиці LMS створено успішно!")
