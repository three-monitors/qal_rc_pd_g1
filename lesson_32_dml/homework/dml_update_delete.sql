-- Встановлюємо схему за замовчуванням
SET search_path TO lesson32, public;

-- Завдання 3. Зміна та видалення

-- 1. Переносимо дедлайн одного завдання на тиждень уперед
UPDATE assignments
SET due_date = due_date + INTERVAL '7 days'
WHERE id = 1
RETURNING id, title, due_date;

-- 2. Оцінюємо усі неоцінені здачі одного завдання. Спочатку переглядаємо через SELECT
SELECT id, assignment_id, student_id, answer_text
FROM submissions
WHERE assignment_id = 2 AND score IS NULL;

-- Потім оцінюємо
UPDATE submissions
SET score = 75
WHERE assignment_id = 2 AND score IS NULL
RETURNING id, assignment_id, student_id, score;

-- 3. Позначаємо один курс неопублікованим (м'яке видалення)
UPDATE courses
SET is_published = FALSE
WHERE id = 3
RETURNING id, title, is_published;

-- 4. Видаляємо тестових студентів. Спочатку видаляємо enrollments
DELETE FROM enrollments
WHERE user_id IN (SELECT id FROM users WHERE email LIKE 'test_%@mail.com');

DELETE FROM submissions
WHERE student_id IN (SELECT id FROM users WHERE email LIKE 'test_%@mail.com');

DELETE FROM users
WHERE email LIKE 'test_%@mail.com'
RETURNING id, first_name, last_name, email;

-- 5. Спробуємо видалити викладача, у якого є курси, і пояснюємо повідомлення про помилку
-- DELETE FROM users WHERE id = 1 AND role = 'teacher';
-- Помилка: FOREIGN KEY constraint — на цього викладача посилаються курси

-- 6. Виконуємо масову зміну всередині транзакції та відкочуємо через ROLLBACK
BEGIN;

UPDATE courses
SET price = price * 1.1;

SELECT id, title, price FROM courses;

ROLLBACK;