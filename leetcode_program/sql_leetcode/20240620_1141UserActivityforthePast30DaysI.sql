-- Select the activity date as 'day' and count the distinct user IDs as 'active_users'
SELECT 
    activity_date AS day, 
    COUNT(DISTINCT user_id) AS active_users
FROM 
    Activity
-- Filter the records to include only those within the last 30 days ending on 2019-07-27
WHERE
    activity_date BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 DAY) AND '2019-07-27'
-- Group the results by activity date
GROUP BY
    activity_date
-- Order the results by activity date in ascending order
ORDER BY
    activity_date ASC;