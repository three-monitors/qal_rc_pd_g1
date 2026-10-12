-- Створення окремої схеми для уроку 32
CREATE SCHEMA IF NOT EXISTS lesson32;

-- Встановлюємо схему за замовчуванням
SET search_path TO lesson32, public;

-- Спочатку залежні таблиці, потім незалежні
DROP TABLE IF EXISTS lesson32.submissions;
DROP TABLE IF EXISTS lesson32.assignments;
DROP TABLE IF EXISTS lesson32.enrollments;
DROP TABLE IF EXISTS lesson32.lessons;
DROP TABLE IF EXISTS lesson32.courses;
DROP TABLE IF EXISTS lesson32.users;

CREATE TABLE IF NOT EXISTS lesson32.users (
    id         INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name  TEXT NOT NULL,
    email      TEXT NOT NULL UNIQUE,
    role       TEXT NOT NULL CHECK (role IN ('student', 'teacher')),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS lesson32.courses (
    id           INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title        TEXT NOT NULL,
    description  TEXT,
    teacher_id   INTEGER NOT NULL,
    is_published BOOLEAN NOT NULL DEFAULT FALSE,
    created_at   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (teacher_id) REFERENCES lesson32.users(id)
);

CREATE TABLE IF NOT EXISTS lesson32.lessons (
    id        INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    course_id INTEGER NOT NULL,
    title     TEXT NOT NULL,
    position  INTEGER NOT NULL CHECK (position > 0),
    content   TEXT,
    FOREIGN KEY (course_id) REFERENCES lesson32.courses(id),
    UNIQUE (course_id, position)
);

CREATE TABLE IF NOT EXISTS lesson32.enrollments (
    user_id     INTEGER NOT NULL,
    course_id   INTEGER NOT NULL,
    enrolled_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status      TEXT NOT NULL DEFAULT 'active'
                CHECK (status IN ('active', 'completed', 'dropped')),
    PRIMARY KEY (user_id, course_id),
    FOREIGN KEY (user_id)   REFERENCES lesson32.users(id),
    FOREIGN KEY (course_id) REFERENCES lesson32.courses(id)
);

CREATE TABLE IF NOT EXISTS lesson32.assignments (
    id        INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    lesson_id INTEGER NOT NULL,
    title     TEXT NOT NULL,
    max_score INTEGER NOT NULL DEFAULT 100 CHECK (max_score > 0),
    due_date  TIMESTAMP,
    FOREIGN KEY (lesson_id) REFERENCES lesson32.lessons(id)
);

CREATE TABLE IF NOT EXISTS lesson32.submissions (
    id            INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    assignment_id INTEGER NOT NULL,
    student_id    INTEGER NOT NULL,
    answer_text   TEXT,
    score         INTEGER CHECK (score >= 0),
    submitted_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (assignment_id) REFERENCES lesson32.assignments(id),
    FOREIGN KEY (student_id)    REFERENCES lesson32.users(id),
    UNIQUE (assignment_id, student_id)
);

-- ALTER TABLE: додаткові колонки
ALTER TABLE lesson32.users ADD COLUMN phone VARCHAR(20);
ALTER TABLE lesson32.courses ADD COLUMN price NUMERIC(10, 2) NOT NULL DEFAULT 0 CHECK (price >= 0);