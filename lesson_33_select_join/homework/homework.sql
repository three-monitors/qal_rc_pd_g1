-- lesson33_homework.sql
-- Автор: <ваше ім'я>

-- Встановлюємо схему за замовчуванням
SET search_path TO lesson33, public;

-- 1. Опубліковані курси дорожчі за 1000, від дорожчих до дешевших
SELECT c.id, c.title, c.price
FROM lesson33.lms_courses AS c
WHERE c.published AND c.price > 1000
ORDER BY c.price DESC;

-- 2. Студенти з e-mail на @example.com, відсортовані за прізвищем
SELECT u.last_name, u.first_name, u.email
FROM lesson33.lms_users AS u
WHERE u.email LIKE '%@example.com'
ORDER BY u.last_name;

-- 3. Три найгірші оцінки (лише виставлені)
SELECT s.id, s.user_id, s.score
FROM lesson33.lms_submissions AS s
WHERE s.score IS NOT NULL
ORDER BY s.score ASC
LIMIT 3;

-- 4. Завдання з max_score не менше 80 і терміном здачі не пізніше 15.10.2026
SELECT a.id, a.title, a.max_score, a.due_date
FROM lesson33.lms_assignments AS a
WHERE a.max_score >= 80 AND a.due_date <= '2026-10-15';

-- 5. Знизити ціну курсу «SQL Basics» на 100 й повернути змінений рядок
BEGIN;
UPDATE lesson33.lms_courses
SET price = price - 100
WHERE title = 'SQL Basics'
RETURNING id, title, price;
ROLLBACK;

-- 6. Позначити запис користувача 5 на курс 1 як completed і повернути рядок
BEGIN;
UPDATE lesson33.lms_enrollments
SET status = 'completed'
WHERE user_id = 5 AND course_id = 1
RETURNING user_id, course_id, status;
ROLLBACK;

-- 7. Видалити відповіді без оцінки до завдання 4 і повернути видалені рядки
BEGIN;
DELETE FROM lesson33.lms_submissions
WHERE assignment_id = 4 AND score IS NULL
RETURNING id, assignment_id, user_id, score;
ROLLBACK;

-- 8. JOIN: назва курсу і прізвище викладача для всіх курсів
SELECT c.title, u.last_name
FROM lesson33.lms_courses AS c
JOIN lesson33.lms_users AS u ON u.id = c.teacher_id;

-- 9. JOIN: студент (прізвище), курс (назва), статус, лише для активних записів
SELECT u.last_name, c.title, e.status
FROM lesson33.lms_enrollments AS e
JOIN lesson33.lms_users AS u ON u.id = e.user_id
JOIN lesson33.lms_courses AS c ON c.id = e.course_id
WHERE e.status = 'active';

-- 10. LEFT JOIN: курси, на які ніхто не записаний
SELECT c.title
FROM lesson33.lms_courses AS c
LEFT JOIN lesson33.lms_enrollments AS e ON e.course_id = c.id
WHERE e.user_id IS NULL;