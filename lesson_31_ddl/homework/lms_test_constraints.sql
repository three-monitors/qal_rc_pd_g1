-- ✅ Коректні дані
INSERT INTO users (first_name, last_name, email, role)
VALUES ('Петро', 'Іваненко', 'petro@lms.ua', 'teacher');

INSERT INTO courses (title, teacher_id)
VALUES ('Python', 1);

INSERT INTO lessons (course_id, title, position, content)
VALUES (1, 'Вступ до Python', 1, 'Основи синтаксису');

INSERT INTO enrollments (user_id, course_id)
VALUES (1, 1);

-- ❌ Дубль email → порушення UNIQUE
INSERT INTO users (first_name, last_name, email, role)
VALUES ('Інший', 'Петро', 'petro@lms.ua', 'teacher');

-- ❌ Роль 'admin' → порушення CHECK
INSERT INTO users (first_name, last_name, email, role)
VALUES ('Ірина', 'Коваль', 'iryna@lms.ua', 'admin');

-- ❌ Викладача 999 не існує → порушення FOREIGN KEY
INSERT INTO courses (title, teacher_id)
VALUES ('SQL', 999);