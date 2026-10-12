-- Встановлюємо схему за замовчуванням
SET search_path TO lesson32, public;

-- Завдання 1. Наповнення

-- 1. Додаємо ще двох студентів і одного викладача в одному INSERT
INSERT INTO users (first_name, last_name, email, role)
VALUES
    ('Віктор', 'Мельник', 'victor@lms.ua', 'teacher'),
    ('Катерина', 'Шевченко', 'katerina@lms.ua', 'student'),
    ('Дмитро', 'Коваль', 'dmytro@lms.ua', 'student');

-- 2. Створюємо для нового викладача курс і три уроки до нього
INSERT INTO courses (title, description, teacher_id, is_published)
VALUES ('Java Basics', 'Основи Java для початківців', 3, TRUE);

INSERT INTO lessons (course_id, title, position)
VALUES
    (5, 'Змінні та типи в Java', 1),
    (5, 'Умови та цикли в Java', 2),
    (5, 'Класи та об''єкти', 3);

-- 3. Записуємо усіх студентів на цей курс одним INSERT ... SELECT
INSERT INTO enrollments (user_id, course_id)
SELECT id, 5
FROM users
WHERE role = 'student'
ON CONFLICT (user_id, course_id) DO NOTHING;

-- 4. Додаємо до курсу завдання і дві здачі
INSERT INTO assignments (lesson_id, title, max_score, due_date)
VALUES (7, 'Hello, Java', 100, '2026-11-15 23:59');

INSERT INTO submissions (assignment_id, student_id, answer_text, score)
VALUES
    (4, 4, 'public class Main { public static void main(String[] args) { System.out.println("Hello"); } }', 85),
    (4, 5, 'public class Main { public static void main(String[] args) { System.out.println("Hello World"); } }', NULL);