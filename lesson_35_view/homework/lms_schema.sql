-- Схема LMS для уроку 35 (така сама, як для уроку 34)

DROP SCHEMA IF EXISTS lesson35 CASCADE;
CREATE SCHEMA lesson35;

SET search_path TO lesson35;

DROP TABLE IF EXISTS submissions;
DROP TABLE IF EXISTS assignments;
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS lessons;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    role VARCHAR(20) NOT NULL CHECK (role IN ('student', 'teacher', 'admin'))
);

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL DEFAULT 0,
    teacher_id INTEGER REFERENCES users(id),
    is_published BOOLEAN DEFAULT FALSE
);

CREATE TABLE lessons (
    id SERIAL PRIMARY KEY,
    course_id INTEGER REFERENCES courses(id),
    title VARCHAR(100) NOT NULL,
    content TEXT,
    order_num INTEGER
);

CREATE TABLE enrollments (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    course_id INTEGER REFERENCES courses(id),
    enrolled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active', 'completed', 'dropped')),
    UNIQUE(user_id, course_id)
);

CREATE TABLE assignments (
    id SERIAL PRIMARY KEY,
    lesson_id INTEGER REFERENCES lessons(id),
    title VARCHAR(100) NOT NULL,
    description TEXT,
    max_score INTEGER DEFAULT 100
);

CREATE TABLE submissions (
    id SERIAL PRIMARY KEY,
    assignment_id INTEGER REFERENCES assignments(id),
    student_id INTEGER REFERENCES users(id),
    content TEXT,
    score INTEGER,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (score IS NULL OR score BETWEEN 0 AND 100)
);

-- Дані

INSERT INTO users (id, first_name, last_name, email, role) VALUES
(1, 'Петро', 'Іваненко', 'petro@lms.ua', 'teacher'),
(2, 'Олена', 'Шевченко', 'olena@lms.ua', 'teacher'),
(3, 'Ірина', 'Коваль', 'iryna@lms.ua', 'student'),
(4, 'Андрій', 'Мельник', 'andriy@lms.ua', 'student'),
(5, 'Марія', 'Бондар', 'maria@lms.ua', 'student'),
(6, 'Тарас', 'Гнатюк', 'taras@lms.ua', 'student'),
(7, 'Софія', 'Лисенко', 'sofia@lms.ua', 'student'),
(8, 'Василь', 'Коваль', 'vasyl@lms.ua', 'teacher');

INSERT INTO courses (id, title, description, price, teacher_id, is_published) VALUES
(1, 'Python Basics', 'Основи Python', 1200.00, 1, TRUE),
(2, 'SQL Basics', 'Основи SQL', 900.00, 1, TRUE),
(3, 'Python Advanced', 'Розширений Python', 1500.00, 2, FALSE),
(4, 'QA Fundamentals', 'Основи тестування', 800.00, 2, TRUE),
(5, 'Git Essentials', 'Основи Git', 0.00, 2, TRUE);

INSERT INTO lessons (id, course_id, title, content, order_num) VALUES
(1, 1, 'Вступ до Python', '...', 1),
(2, 1, 'Змінні та типи', '...', 2),
(3, 1, 'Цикли', '...', 3),
(4, 2, 'Вступ до SQL', '...', 1),
(5, 2, 'SELECT', '...', 2),
(6, 2, 'JOIN', '...', 3),
(7, 4, 'Тест-кейс для форми', '...', 1),
(8, 4, 'Тестування API', '...', 2);

INSERT INTO assignments (id, lesson_id, title, description, max_score) VALUES
(1, 1, 'Hello, Python', '...', 100),
(2, 3, 'Цикли', '...', 100),
(3, 2, 'Функція-калькулятор', '...', 100),
(4, 4, 'Перші запити', '...', 50),
(5, 5, 'JOIN-и', '...', 50),
(6, 7, 'Тест-кейс для форми', '...', 100);

INSERT INTO enrollments (id, user_id, course_id, status) VALUES
(1, 3, 1, 'active'),
(2, 3, 2, 'active'),
(3, 4, 1, 'active'),
(4, 4, 4, 'completed'),
(5, 5, 1, 'active'),
(6, 5, 2, 'dropped'),
(7, 5, 4, 'active'),
(8, 7, 2, 'active'),
(9, 7, 4, 'active');

INSERT INTO submissions (id, assignment_id, student_id, content, score, submitted_at) VALUES
(1, 1, 3, '...', 90, '2026-10-01 10:00'),
(2, 1, 4, '...', 70, '2026-10-02 12:30'),
(3, 1, 5, '...', 100, '2026-10-02 09:15'),
(4, 2, 3, '...', 85, '2026-10-08 18:00'),
(5, 2, 4, '...', NULL, '2026-10-09 11:00'),
(6, 3, 3, '...', NULL, '2026-10-10 20:45'),
(7, 4, 3, '...', 45, '2026-10-12 14:20'),
(8, 4, 7, '...', 50, '2026-10-13 16:10'),
(9, 6, 4, '...', 80, '2026-10-14 13:00'),
(10, 6, 7, '...', NULL, '2026-10-15 17:30');

-- VIEW з лекції (потрібні для завдань 21-24)

CREATE VIEW v_course_overview AS
SELECT
    c.id AS course_id,
    c.title,
    c.price,
    c.is_published,
    t.first_name || ' ' || t.last_name AS teacher,
    (SELECT COUNT(*) FROM lessons l WHERE l.course_id = c.id) AS lessons_count,
    (SELECT COUNT(*) FROM enrollments e WHERE e.course_id = c.id AND e.status = 'active') AS active_students
FROM courses c
JOIN users t ON t.id = c.teacher_id;

CREATE VIEW v_gradebook AS
SELECT
    s.id AS submission_id,
    st.id AS student_id,
    st.first_name || ' ' || st.last_name AS student,
    c.id AS course_id,
    c.title AS course,
    a.title AS assignment,
    s.score,
    a.max_score,
    ROUND(100.0 * s.score / a.max_score, 1) AS percent,
    s.submitted_at
FROM submissions s
JOIN users st ON st.id = s.student_id
JOIN assignments a ON a.id = s.assignment_id
JOIN lessons l ON l.id = a.lesson_id
JOIN courses c ON c.id = l.course_id;