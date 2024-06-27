-- # Write your MySQL query statement below
-- SELECT
--     *
-- -- SELECT 
-- --     U.contest_id, 
-- --     U.percentage    
-- FROM 
--     Users U
-- LEFT JOIN
--     Register R
-- ON
--     U.user_id = R.user_id
-- -- GROUP BY
-- --     U.contest_id,
-- --     U.user_id
-- --     ;
-- ORDER BY
--     contest_id


SELECT
    R.contest_id,
    ROUND(COUNT(DISTINCT R.user_id) / T.total_users * 100, 2) AS percentage
FROM
    Register R
JOIN
    (SELECT COUNT(*) AS total_users FROM Users) T
ON
    1 = 1
GROUP BY
    R.contest_id
ORDER BY
    percentage DESC,
    R.contest_id ASC;
