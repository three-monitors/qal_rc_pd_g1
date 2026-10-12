-- Встановлюємо схему за замовчуванням
SET search_path TO lesson32, public;

-- Завдання 2. Пошук

-- 1. Усі курси, у назві яких є слово Python, незалежно від регістру
SELECT id, title, price
FROM courses
WHERE title ILIKE '%Python%';

-- 2. Усіх студентів з поштою не на gmail.com
SELECT id, first_name, last_name, email
FROM users
WHERE role = 'student' AND email NOT LIKE '%@gmail.com';

-- 3. Усі здачі, які ще не оцінені
SELECT id, assignment_id, student_id, submitted_at
FROM submissions
WHERE score IS NULL;

-- 4. Три найвищі оцінки. NULL не повинні потрапити в результат
SELECT id, assignment_id, student_id, score
FROM submissions
WHERE score IS NOT NULL
ORDER BY score DESC NULLS LAST
LIMIT 3;

-- 5. Друга сторінка списку користувачів, відсортованих за прізвищем, по 3 записи на сторінку
SELECT id, first_name, last_name, email
FROM users
ORDER BY last_name
LIMIT 3 OFFSET 3;