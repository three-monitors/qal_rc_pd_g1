-- Встановлюємо схему за замовчуванням
SET search_path TO lesson33, public;

-- Додатково: завдання, до яких немає жодної відповіді студента
SELECT a.id, a.title
FROM lesson33.lms_assignments AS a
LEFT JOIN lesson33.lms_submissions AS s ON s.assignment_id = a.id
WHERE s.id IS NULL;