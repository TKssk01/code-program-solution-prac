# Write your MySQL query statement below
WITH ConfirmCounts as{
    SELECT
        product_id,
        COUNT(product_id) as total_requests
        SUM(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END) AS confirmed_requests,
        MIN(time_stamp) as first_request_time
    FROM
        Confirmations
    GROUP BY
        user_id
}

SELECT
    S.user_id,
    ROUND(C.confirmed_requests, 0)/ COALESCE(C.total_requests, 1), 2) as confirmation_rate
-- SELECT
--     *
FROM
    Signups S
LEFT JOIN
    ConfirmCounts C
ON
    S.user_id = C.user_id
ORDER BY
    CASE WHEN ROUND(C.confirmed_requests, 0)/ COALESCE(C.total_requests, 1), 2) = 0 THEN 0 ELSE 1 END ASC,
    confirmation_rate DESC,
    first_request_time ASC,
    S.user_id;
