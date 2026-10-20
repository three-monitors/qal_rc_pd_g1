-- Встановлюємо схему за замовчуванням
SET search_path TO lesson32, public;

-- Завдання 4. Індекси

-- 1. Створюємо індекси на зовнішніх ключах, де їх бракує
CREATE INDEX idx_courses_teacher_id ON lesson32.courses (teacher_id);
CREATE INDEX idx_lessons_course_id ON lesson32.lessons (course_id);
CREATE INDEX idx_enrollments_user_id ON lesson32.enrollments (user_id);
CREATE INDEX idx_enrollments_course_id ON lesson32.enrollments (course_id);
CREATE INDEX idx_assignments_lesson_id ON lesson32.assignments (lesson_id);
CREATE INDEX idx_submissions_assignment_id ON lesson32.submissions (assignment_id);
CREATE INDEX idx_submissions_student_id ON lesson32.submissions (student_id);

-- 2. Генеруємо 100 000 тестових користувачів
INSERT INTO lesson32.users (first_name, last_name, email, role)
SELECT 'User' || g, 'Load', 'user' || g || '@load.test', 'student'
FROM generate_series(1, 100000) AS g;

-- 3. Порівнюємо EXPLAIN ANALYZE для пошуку за неіндексованою колонкою до і після створення індексу
-- До індексу:
EXPLAIN ANALYZE
SELECT * FROM lesson32.users WHERE first_name = 'User77777';

-- Створюємо індекс
CREATE INDEX idx_users_first_name ON lesson32.users (first_name);

-- Після індексу:
EXPLAIN ANALYZE
SELECT * FROM lesson32.users WHERE first_name = 'User77777';

-- 4. Переглядаємо індекси таблиці users через pg_indexes
SELECT indexname, indexdef
FROM pg_indexes
WHERE tablename = 'users' AND schemaname = 'lesson32';

-- 5. Видаляємо тестові дані та експериментальний індекс
DELETE FROM lesson32.users WHERE email LIKE '%@load.test';
DROP INDEX IF EXISTS idx_users_first_name;