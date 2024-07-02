# Write your MySQL query statement below
-- SELECT *
SELECT
    teacher_id,
    COUNT(DISTINCT subject_id) AS cnt
FROM
    Teacher
GROUP BY
    -- dept_id
    -- subject_id,
    teacher_id;
