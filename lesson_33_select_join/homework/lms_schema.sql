-- Створення окремої схеми для уроку 33
CREATE SCHEMA IF NOT EXISTS lesson33;

-- Встановлюємо схему за замовчуванням
SET search_path TO lesson33, public;

-- Навчальна база LMS для заняття 33
DROP TABLE IF EXISTS lesson33.lms_submissions, lesson33.lms_assignments, lesson33.lms_enrollments,
                     lesson33.lms_lessons, lesson33.lms_courses, lesson33.lms_users CASCADE;

CREATE TABLE lesson33.lms_users (
    id         INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name  VARCHAR(100) NOT NULL,
    email      VARCHAR(255) NOT NULL UNIQUE,
    role       VARCHAR(20)  NOT NULL CHECK (role IN ('student', 'teacher')),
    created_at TIMESTAMP    NOT NULL DEFAULT now()
);

CREATE TABLE lesson33.lms_courses (
    id          INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title       VARCHAR(200) NOT NULL,
    description TEXT,
    teacher_id  INTEGER NOT NULL REFERENCES lesson33.lms_users(id),
    published   BOOLEAN NOT NULL DEFAULT FALSE,
    price       NUMERIC(10, 2) NOT NULL DEFAULT 0 CHECK (price >= 0),
    created_at  TIMESTAMP NOT NULL DEFAULT now()
);

CREATE TABLE lesson33.lms_lessons (
    id        INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    course_id INTEGER NOT NULL REFERENCES lesson33.lms_courses(id) ON DELETE CASCADE,
    title     VARCHAR(200) NOT NULL,
    position  INTEGER NOT NULL CHECK (position > 0),
    content   TEXT
);

CREATE TABLE lesson33.lms_enrollments (
    user_id     INTEGER NOT NULL REFERENCES lesson33.lms_users(id),
    course_id   INTEGER NOT NULL REFERENCES lesson33.lms_courses(id),
    status      VARCHAR(20) NOT NULL DEFAULT 'active'
                CHECK (status IN ('active', 'completed', 'dropped')),
    enrolled_at TIMESTAMP NOT NULL DEFAULT now(),
    PRIMARY KEY (user_id, course_id)
);

CREATE TABLE lesson33.lms_assignments (
    id        INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    lesson_id INTEGER NOT NULL REFERENCES lesson33.lms_lessons(id) ON DELETE CASCADE,
    title     VARCHAR(200) NOT NULL,
    max_score INTEGER NOT NULL DEFAULT 100,
    due_date  DATE
);

CREATE TABLE lesson33.lms_submissions (
    id            INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    assignment_id INTEGER NOT NULL REFERENCES lesson33.lms_assignments(id),
    user_id       INTEGER NOT NULL REFERENCES lesson33.lms_users(id),
    answer        TEXT,
    score         INTEGER CHECK (score BETWEEN 0 AND 100),
    submitted_at  TIMESTAMP NOT NULL DEFAULT now()
);

-- Користувачі: 2 викладачі (id 1, 2) і 4 студенти (id 3-6)
INSERT INTO lesson33.lms_users (first_name, last_name, email, role) VALUES
    ('Петро',  'Іваненко', 'p.ivanenko@example.com',   'teacher'),
    ('Олена',  'Шевченко', 'o.shevchenko@example.com', 'teacher'),
    ('Ірина',  'Коваль',   'i.koval@example.com',      'student'),
    ('Андрій', 'Мельник',  'a.melnyk@example.com',     'student'),
    ('Ігор',   'Петренко', 'i.petrenko@example.com',   'student'),
    ('Марія',  'Бондар',   'm.bondar@example.com',     'student');

-- Курси: Docker не опублікований, на Docker і Django ніхто не записаний
INSERT INTO lesson33.lms_courses (title, description, teacher_id, published, price) VALUES
    ('Python Basics', 'Основи Python', 1, TRUE,  1500.00),
    ('SQL Basics',    'Основи SQL',    2, TRUE,  1200.00),
    ('Docker Basics', NULL,            1, FALSE, 0),
    ('Django',        'Веб на Django', 2, TRUE,  2000.00);

INSERT INTO lesson33.lms_lessons (course_id, title, position) VALUES
    (1, 'Hello Python', 1),
    (1, 'Variables and types', 2),
    (1, 'Loops', 3),
    (2, 'Hello SQL', 1),
    (2, 'SELECT basics', 2),
    (3, 'What is Docker', 1);

INSERT INTO lesson33.lms_enrollments (user_id, course_id, status) VALUES
    (3, 1, 'active'),
    (3, 2, 'active'),
    (4, 1, 'completed'),
    (5, 2, 'active'),
    (5, 1, 'dropped'),
    (6, 2, 'active');

INSERT INTO lesson33.lms_assignments (lesson_id, title, max_score, due_date) VALUES
    (1, 'Hello world',     100, '2026-10-05'),
    (2, 'Types quiz',       50, '2026-10-12'),
    (3, 'Loops task',      100, '2026-10-20'),
    (4, 'Create table',    100, '2026-10-10'),
    (5, 'Select practice',  80, '2026-10-30'),
    (6, 'Docker intro',    100, '2026-11-05');

-- Відповіді: у деяких score = NULL (ще не оцінено)
INSERT INTO lesson33.lms_submissions (assignment_id, user_id, answer, score) VALUES
    (1, 3, 'print("Hello")', 95),
    (1, 4, 'print("Hi")',    70),
    (2, 3, 'quiz answers',   45),
    (2, 4, 'quiz answers',   NULL),
    (4, 3, 'CREATE TABLE',   88),
    (4, 5, 'CREATE TABLE',   65),
    (4, 6, 'CREATE TABLE',   NULL),
    (5, 3, 'SELECT *',       NULL);