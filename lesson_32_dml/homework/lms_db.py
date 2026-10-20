import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

DSN = os.getenv("DATABASE_URL")


def add_user(first_name: str, last_name: str, email: str, role: str):
    """INSERT: створити користувача і повернути його id."""
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """INSERT INTO lesson32.users (first_name, last_name, email, role)
                   VALUES (%s, %s, %s, %s)
                   RETURNING id, email;""",
                (first_name, last_name, email, role),
            )
            return cur.fetchone()


def get_course(course_id: int):
    """SELECT: отримати курс за id."""
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, title, price, is_published FROM lesson32.courses WHERE id = %s;",
                (course_id,),
            )
            return cur.fetchone()


def enroll_student(user_id: int, course_id: int):
    """INSERT: записати студента на курс."""
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """INSERT INTO lesson32.enrollments (user_id, course_id)
                   VALUES (%s, %s)
                   ON CONFLICT (user_id, course_id) DO NOTHING
                   RETURNING user_id, course_id;""",
                (user_id, course_id),
            )
            return cur.fetchone()


def grade_submission(assignment_id: int, student_id: int, score: int):
    """UPDATE: оцінити здачу."""
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """UPDATE lesson32.submissions SET score = %s
                   WHERE assignment_id = %s AND student_id = %s AND score IS NULL
                   RETURNING id, assignment_id, student_id, score;""",
                (score, assignment_id, student_id),
            )
            return cur.fetchone()


def search_courses(term: str, page: int = 1, per_page: int = 10):
    """Пошук за назвою (без урахування регістру) з пагінацією."""
    pattern = f"%{term}%"
    offset = (page - 1) * per_page

    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT COUNT(*) FROM lesson32.courses WHERE title ILIKE %s;",
                (pattern,),
            )
            total = cur.fetchone()[0]

            cur.execute(
                """SELECT id, title, price
                   FROM lesson32.courses
                   WHERE title ILIKE %s
                   ORDER BY created_at DESC, id
                   LIMIT %s OFFSET %s;""",
                (pattern, per_page, offset),
            )
            courses = cur.fetchall()

    return {
        "courses": courses,
        "total": total,
        "page": page,
        "total_pages": (total + per_page - 1) // per_page,
    }


if __name__ == "__main__":
    # Тестування функцій
    print("Тестування add_user:")
    user = add_user("Тест", "Користувач", "test@test.com", "student")
    print(f"  Створено: {user}")

    print("\nТестування get_course:")
    course = get_course(1)
    print(f"  Курс: {course}")

    print("\nТестування enroll_student:")
    enrollment = enroll_student(3, 1)
    print(f"  Запис: {enrollment}")

    print("\nТестування grade_submission:")
    grade = grade_submission(2, 3, 80)
    print(f"  Оцінка: {grade}")

    print("\nТестування search_courses:")
    result = search_courses("python", page=1, per_page=10)
    print(f"  Знайдено курсів: {result['total']}")
    for course_id, title, price in result["courses"]:
        print(f"    {course_id}. {title}: {price}")
