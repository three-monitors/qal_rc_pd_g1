-- Спочатку залежні таблиці, потім незалежні
DROP TABLE IF EXISTS submissions;
DROP TABLE IF EXISTS assignments;
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS lessons;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS users;

-- Таблиця користувачів
CREATE TABLE users (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    role TEXT NOT NULL CHECK (role IN ('student', 'teacher')),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Таблиця курсів
CREATE TABLE courses (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    teacher_id INTEGER NOT NULL,
    is_published BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (teacher_id) REFERENCES users(id)
);

-- Таблиця уроків
CREATE TABLE lessons (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    course_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    position INTEGER NOT NULL CHECK (position > 0),
    content TEXT,
    FOREIGN KEY (course_id) REFERENCES courses(id),
    UNIQUE (course_id, position)
);

-- Таблиця записів на курси (M:N)
CREATE TABLE enrollments (
    user_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    enrolled_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'completed', 'dropped')),
    PRIMARY KEY (user_id, course_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

-- Таблиця завдань
CREATE TABLE assignments (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    lesson_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    max_score INTEGER NOT NULL DEFAULT 100 CHECK (max_score > 0),
    due_date TIMESTAMP,
    FOREIGN KEY (lesson_id) REFERENCES lessons(id)
);

-- Таблиця здач завдань (M:N)
CREATE TABLE submissions (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    assignment_id INTEGER NOT NULL,
    student_id INTEGER NOT NULL,
    answer_text TEXT,
    score INTEGER CHECK (score >= 0),
    submitted_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (assignment_id) REFERENCES assignments(id),
    FOREIGN KEY (student_id) REFERENCES users(id),
    UNIQUE (assignment_id, student_id)
);