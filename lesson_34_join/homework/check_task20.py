import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

dsn = os.getenv("DATABASE_URL")

with psycopg.connect(dsn) as conn:
    with conn.cursor() as cur:
        # Перевіряємо email викладача Олени
        cur.execute(
            "SELECT id, first_name, last_name, email FROM lesson34.users WHERE email = 'olena@lms.ua';")
        print("Викладач Олена (users):")
        print(cur.fetchone())

        # Перевіряємо які курси веде Олена
        cur.execute(
            "SELECT id, title, teacher_id FROM lesson34.courses WHERE teacher_id = 2;")
        print("\nКурси Олени (courses):")
        for row in cur.fetchall():
            print(row)

        # Перевіряємо всі неоцінені здачі
        cur.execute(
            "SELECT id, assignment_id, student_id FROM lesson34.submissions WHERE score IS NULL;")
        print("\nНеоцінені здачі (submissions):")
        for row in cur.fetchall():
            print(row)

        # Перевіряємо здачу 10
        cur.execute("""
            SELECT s.id, st.first_name, st.last_name, st.email, c.title, a.title
            FROM lesson34.submissions s
            JOIN lesson34.users st ON st.id = s.student_id
            JOIN lesson34.assignments a ON a.id = s.assignment_id
            JOIN lesson34.lessons l ON l.id = a.lesson_id
            JOIN lesson34.courses c ON c.id = l.course_id
            WHERE s.id = 10;
        """)
        print("\nЗдача 10:")
        print(cur.fetchone())
