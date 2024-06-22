SELECT
    user_id,
    COUNT(follower_id) as followers_count
FROM
    Followers
-- user_idごとにグループ化
GROUP BY
    user_id
ORDER BY
    user_id ASC;
