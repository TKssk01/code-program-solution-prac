# Write your MySQL query statement below
SELECT
    project_id,
    AVG(experience_years) as average_years
-- SELECT
--     *
FROM
    Project p
LEFT JOIN
    Employee E
ON
    P.employee_id = E.employee_id
Group by
    project_id