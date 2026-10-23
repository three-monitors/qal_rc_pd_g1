-- Встановлюємо схему lesson35 для всіх запитів
SET search_path TO lesson35;

-- Рівень 1. Агрегати, GROUP BY, HAVING

-- 1. Скільки всього користувачів, студентів і викладачів. Виведіть кількість за кожною роллю.
SELECT role, COUNT(*) AS cnt
FROM users
GROUP BY role
ORDER BY role;

-- 2. Мінімальна, максимальна й середня ціна курсів.
SELECT
    MIN(price) AS min_price,
    MAX(price) AS max_price,
    ROUND(AVG(price), 2) AS avg_price
FROM courses;

-- 3. Кількість здач на кожне завдання.
SELECT assignment_id, COUNT(*) AS submissions
FROM submissions
GROUP BY assignment_id
ORDER BY assignment_id;

-- 4. Для кожного студента (ім'я та прізвище): кількість здач і середня оцінка.
-- Залишіть лише студентів, які здали щонайменше 2 роботи. Сортуйте за кількістю здач за спаданням.
SELECT
    u.first_name || ' ' || u.last_name AS student,
    COUNT(*) AS submissions,
    ROUND(AVG(s.score), 2) AS avg_score
FROM submissions s
JOIN users u ON u.id = s.student_id
GROUP BY u.id, u.first_name, u.last_name
HAVING COUNT(*) >= 2
ORDER BY submissions DESC;

-- 5. Для кожного завдання виведіть кількість оцінених і неоцінених здач (використайте FILTER).
SELECT
    assignment_id,
    COUNT(*) FILTER (WHERE score IS NOT NULL) AS graded,
    COUNT(*) FILTER (WHERE score IS NULL) AS pending
FROM submissions
GROUP BY assignment_id
ORDER BY assignment_id;

-- 6. Кількість активних записів на кожен курс. Залишіть лише курси, де їх не менше двох.
SELECT
    c.title,
    COUNT(e.user_id) AS active_students
FROM courses c
LEFT JOIN enrollments e ON e.course_id = c.id AND e.status = 'active'
GROUP BY c.id, c.title
HAVING COUNT(e.user_id) >= 2
ORDER BY c.id;

-- 7. Для кожного викладача (включно з тими, у кого немає курсів): кількість курсів і сума цін курсів (0, якщо курсів немає).
SELECT
    u.first_name || ' ' || u.last_name AS teacher,
    COUNT(c.id) AS courses_count,
    COALESCE(SUM(c.price), 0) AS total_price
FROM users u
LEFT JOIN courses c ON c.teacher_id = u.id
WHERE u.role = 'teacher'
GROUP BY u.id, u.first_name, u.last_name
ORDER BY u.id;

-- Рівень 2. Вкладені запити та DISTINCT

-- 8. Курси, дорожчі за середню ціну.
SELECT title, price
FROM courses
WHERE price > (SELECT AVG(price) FROM courses)
ORDER BY price DESC;

-- 9. Студенти, які не здали жодної роботи (NOT EXISTS).
SELECT id, first_name, last_name
FROM users
WHERE role = 'student'
  AND NOT EXISTS (SELECT 1 FROM submissions s WHERE s.student_id = users.id)
ORDER BY id;

-- 10. Курси, у яких є хоча б одне завдання (EXISTS, шлях через lessons та assignments).
SELECT c.id, c.title
FROM courses c
WHERE EXISTS (
    SELECT 1
    FROM lessons l
    JOIN assignments a ON a.lesson_id = l.id
    WHERE l.course_id = c.id
)
ORDER BY c.id;

-- 11. Здачі з оцінкою вищою за середню по своєму завданню (корельований підзапит).
SELECT s.id, s.assignment_id, s.score
FROM submissions s
WHERE s.score > (
    SELECT AVG(s2.score)
    FROM submissions s2
    WHERE s2.assignment_id = s.assignment_id
)
ORDER BY s.id;

-- 12. Середня кількість здач на студента (серед тих, хто здавав), підзапит у FROM.
SELECT ROUND(AVG(cnt), 2) AS avg_submissions_per_student
FROM (
    SELECT student_id, COUNT(*) AS cnt
    FROM submissions
    GROUP BY student_id
) AS per_student;

-- 13. Унікальні пари «викладач, опубліковано» з таблиці courses.
SELECT DISTINCT teacher_id, is_published
FROM courses
ORDER BY teacher_id, is_published;

-- 14. Остання здача кожного студента (DISTINCT ON).
SELECT DISTINCT ON (student_id)
    student_id, id AS submission_id, submitted_at, score
FROM submissions
ORDER BY student_id, submitted_at DESC;

-- 15. Найкраща здача кожного завдання (DISTINCT ON, NULL в кінці).
SELECT DISTINCT ON (assignment_id)
    assignment_id, id AS submission_id, student_id, score
FROM submissions
ORDER BY assignment_id, score DESC NULLS LAST, id;

-- Рівень 3. Віконні функції

-- 16. Усі здачі з середньою оцінкою завдання та відхиленням від неї.
SELECT
    id,
    assignment_id,
    score,
    ROUND(AVG(score) OVER (PARTITION BY assignment_id), 2) AS assignment_avg,
    ROUND(score - AVG(score) OVER (PARTITION BY assignment_id), 2) AS diff
FROM submissions
ORDER BY id;

-- 17. Для кожного завдання місце студента серед оцінених робіт (RANK). Залишіть лише першу позицію.
WITH ranked AS (
    SELECT
        assignment_id,
        student_id,
        score,
        RANK() OVER (
            PARTITION BY assignment_id
            ORDER BY score DESC NULLS LAST
        ) AS place
    FROM submissions
    WHERE score IS NOT NULL
)
SELECT assignment_id, student_id, score
FROM ranked
WHERE place = 1
ORDER BY assignment_id;

-- 18. Накопичувальна сума балів кожного студента за часом здачі.
SELECT
    student_id,
    id,
    submitted_at::date AS day,
    score,
    SUM(score) OVER (
        PARTITION BY student_id
        ORDER BY submitted_at
    ) AS running_sum
FROM submissions
ORDER BY student_id, submitted_at;

-- 19. Для кожної оціненої здачі: попередня оцінка того ж студента (LAG) і зміна.
SELECT
    student_id,
    id,
    score,
    LAG(score) OVER w AS prev_score,
    score - LAG(score) OVER w AS change
FROM submissions
WHERE score IS NOT NULL
WINDOW w AS (PARTITION BY student_id ORDER BY submitted_at)
ORDER BY student_id, submitted_at;

-- 20. Порядковий номер здачі кожного студента за часом (ROW_NUMBER). Виведіть студентів, які мають четверту здачу.
WITH numbered AS (
    SELECT
        student_id,
        ROW_NUMBER() OVER (PARTITION BY student_id ORDER BY submitted_at) AS row_num
    FROM submissions
)
SELECT DISTINCT student_id
FROM numbered
WHERE row_num = 4
ORDER BY student_id;

-- Рівень 4. VIEW

-- 21. Створіть v_student_progress (студент, курс, кількість оцінених робіт, середня оцінка) на основі v_gradebook.
CREATE VIEW v_student_progress AS
SELECT
    student_id,
    student,
    course_id,
    course,
    COUNT(score) AS graded_count,
    ROUND(AVG(score), 2) AS avg_score
FROM v_gradebook
GROUP BY student_id, student, course_id, course;

-- Скільки в ньому рядків?
-- SELECT COUNT(*) FROM v_student_progress; -- очікується 7

-- 22. На основі v_course_overview знайдіть курси без жодного активного студента.
SELECT title, active_students
FROM v_course_overview
WHERE active_students = 0
ORDER BY course_id;

-- 23. Створіть v_pending_review (здачі без оцінки: id здачі, teacher_id, студент, курс, завдання, час здачі).
CREATE VIEW v_pending_review AS
SELECT
    s.id AS submission_id,
    c.teacher_id,
    st.first_name || ' ' || st.last_name AS student,
    c.title AS course,
    a.title AS assignment,
    s.submitted_at
FROM submissions s
JOIN users st ON st.id = s.student_id
JOIN assignments a ON a.id = s.assignment_id
JOIN lessons l ON l.id = a.lesson_id
JOIN courses c ON c.id = l.course_id
WHERE s.score IS NULL;

-- Виберіть із неї роботи, що чекають на перевірку викладача Петра (id 1).
SELECT submission_id, student, course, assignment, submitted_at
FROM v_pending_review
WHERE teacher_id = 1
ORDER BY submitted_at;

-- 24. Створіть mv_course_scores.
CREATE MATERIALIZED VIEW mv_course_scores AS
SELECT
    course_id,
    course,
    COUNT(score) AS graded,
    ROUND(AVG(score), 2) AS avg_score
FROM v_gradebook
GROUP BY course_id, course;
 
-- Потім змініть оцінку здачі 5 на 60, перегляньте v_gradebook і mv_course_scores,
-- виконайте REFRESH і порівняйте. Усередині транзакції з ROLLBACK, щоб повернути дані.
BEGIN;
UPDATE submissions SET score = 60 WHERE id = 5;
SELECT * FROM v_gradebook WHERE assignment = 'Цикли';
SELECT * FROM mv_course_scores WHERE course_id = 1;
REFRESH MATERIALIZED VIEW mv_course_scores;
SELECT * FROM mv_course_scores WHERE course_id = 1;
ROLLBACK;