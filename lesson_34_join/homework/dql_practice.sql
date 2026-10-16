-- Встановлюємо схему за замовчуванням
SET search_path TO lesson34, public;

-- Рівень 1. Одна таблиця

-- 1. Виведіть назви та ціни всіх курсів, від найдорожчого до найдешевшого
SELECT c.title, c.price
FROM lesson34.courses AS c
ORDER BY c.price DESC;

-- 2. Виведіть опубліковані курси з ціною не більше 1000
SELECT c.title, c.price
FROM lesson34.courses AS c
WHERE c.is_published = TRUE AND c.price <= 1000;

-- 3. Виведіть користувачів із поштою на lms.ua
SELECT u.first_name, u.last_name, u.email
FROM lesson34.users AS u
WHERE u.email LIKE '%@lms.ua';

-- 4. Виведіть курси, у яких немає опису
SELECT c.title
FROM lesson34.courses AS c
WHERE c.description IS NULL;

-- 5. Виведіть студентів, пошта яких не на gmail.com
SELECT u.first_name, u.last_name, u.email
FROM lesson34.users AS u
WHERE u.role = 'student' AND u.email NOT LIKE '%@gmail.com';

-- 6. Виведіть завдання без дедлайну
SELECT a.id, a.title
FROM lesson34.assignments AS a
WHERE a.due_date IS NULL;

-- 7. Виведіть здачі, які ще не оцінені
SELECT s.id, s.assignment_id, s.student_id
FROM lesson34.submissions AS s
WHERE s.score IS NULL;

-- 8. Виведіть три найновіші здачі
SELECT s.id, s.submitted_at
FROM lesson34.submissions AS s
ORDER BY s.submitted_at DESC
LIMIT 3;

-- 9. Виведіть другу сторінку курсів (по 2 на сторінці, сортування за id)
SELECT c.id, c.title
FROM lesson34.courses AS c
ORDER BY c.id
LIMIT 2 OFFSET 2;

-- 10. Виведіть курси з ціною від 800 до 1200 включно
SELECT c.title, c.price
FROM lesson34.courses AS c
WHERE c.price BETWEEN 800 AND 1200;

-- 11. Знайдіть курси, у назві яких є слово basics, незалежно від регістру
SELECT c.title
FROM lesson34.courses AS c
WHERE c.title ILIKE '%basics%';

-- Рівень 2. JOIN

-- 12. Виведіть усі курси разом з іменем та прізвищем викладача (INNER JOIN)
SELECT c.id, c.title, u.first_name, u.last_name
FROM lesson34.courses AS c
JOIN lesson34.users AS u ON u.id = c.teacher_id;

-- 13. Виведіть усі уроки з назвою курсу, відсортовані за курсом і позицією
SELECT c.title AS course, l.position, l.title AS lesson
FROM lesson34.lessons AS l
JOIN lesson34.courses AS c ON c.id = l.course_id
ORDER BY c.id, l.position;

-- 14. Виведіть активних студентів кожного курсу (назва курсу, ім'я, прізвище)
SELECT c.title AS course, u.first_name, u.last_name
FROM lesson34.enrollments AS e
JOIN lesson34.users AS u ON u.id = e.user_id
JOIN lesson34.courses AS c ON c.id = e.course_id
WHERE e.status = 'active'
ORDER BY c.id, u.id;

-- 15. Знайдіть курси без жодного уроку
SELECT c.id, c.title
FROM lesson34.courses AS c
LEFT JOIN lesson34.lessons AS l ON l.course_id = c.id
WHERE l.id IS NULL;

-- 16. Знайдіть студентів, які не записані ні на один курс
SELECT u.id, u.first_name, u.last_name
FROM lesson34.users AS u
LEFT JOIN lesson34.enrollments AS e ON e.user_id = u.id
WHERE u.role = 'student' AND e.user_id IS NULL;

-- 17. Знайдіть викладачів, у яких немає курсів
SELECT u.id, u.first_name, u.last_name
FROM lesson34.users AS u
LEFT JOIN lesson34.courses AS c ON c.teacher_id = u.id
WHERE u.role = 'teacher' AND c.id IS NULL;

-- 18. Виведіть усі курси та кількість активних студентів на кожному, включно з нулями
SELECT c.title, COUNT(e.user_id) AS students
FROM lesson34.courses AS c
LEFT JOIN lesson34.enrollments AS e
       ON e.course_id = c.id AND e.status = 'active'
GROUP BY c.id, c.title
ORDER BY c.id;

-- 19. Знайдіть завдання, на які ще ніхто не здав роботу
SELECT a.id, a.title
FROM lesson34.assignments AS a
LEFT JOIN lesson34.submissions AS s ON s.assignment_id = a.id
WHERE s.id IS NULL;

-- Рівень 3. Складні вибірки

-- 20. Для викладача Олени (olena@lms.ua) виведіть неоцінені здачі: студент, курс, завдання
SELECT st.first_name || ' ' || st.last_name AS student, c.title AS course, a.title AS assignment
FROM lesson34.submissions AS s
JOIN lesson34.users AS st ON st.id = s.student_id
JOIN lesson34.assignments AS a ON a.id = s.assignment_id
JOIN lesson34.lessons AS l ON l.id = a.lesson_id
JOIN lesson34.courses AS c ON c.id = l.course_id
JOIN lesson34.users AS u ON u.id = c.teacher_id
WHERE s.score IS NULL AND u.email = 'olena@lms.ua';

-- 21. Виведіть журнал студентки Ірини (iryna@mail.com): курс, завдання, оцінка, максимальний бал, оцінка у відсотках
SELECT c.title AS course, a.title AS assignment, s.score, a.max_score, ROUND(100.0 * s.score / a.max_score, 1) AS percentage
FROM lesson34.submissions AS s
JOIN lesson34.assignments AS a ON a.id = s.assignment_id
JOIN lesson34.lessons AS l ON l.id = a.lesson_id
JOIN lesson34.courses AS c ON c.id = l.course_id
JOIN lesson34.users AS u ON u.id = s.student_id
WHERE u.email = 'iryna@mail.com'
ORDER BY s.id;

-- 22. Виведіть трьох студентів із найбільшою сумою оцінок
SELECT st.first_name || ' ' || st.last_name AS student, SUM(s.score) AS total_score
FROM lesson34.submissions AS s
JOIN lesson34.users AS st ON st.id = s.student_id
GROUP BY st.id, st.first_name, st.last_name
ORDER BY total_score DESC
LIMIT 3;

-- 23. Для кожного курсу виведіть кількість здач і середню оцінку, включно з курсами без жодної здачі
SELECT c.title, COUNT(s.id) AS submissions, ROUND(AVG(s.score), 2) AS avg_score
FROM lesson34.courses AS c
LEFT JOIN lesson34.lessons AS l ON l.course_id = c.id
LEFT JOIN lesson34.assignments AS a ON a.lesson_id = l.id
LEFT JOIN lesson34.submissions AS s ON s.assignment_id = a.id
GROUP BY c.id, c.title
ORDER BY c.id;