-- 各ユーザーの友達数を集計
-- 友達関係のリストを作成
WITH Friends AS (
    -- リクエストを送ったユーザーIDを集める
    SELECT requester_id AS user_id
    FROM RequestAccepted
    UNION ALL
    -- リクエストを受け入れたユーザーIDを集める
    SELECT accepter_id AS user_id
    FROM RequestAccepted
),
-- 各ユーザーの友達数をカウント
FriendCount AS (
    -- ユーザーIDごとに友達数をカウントする
    SELECT user_id, COUNT(*) AS num_friends
    FROM Friends
    GROUP BY user_id
)

-- 最も多くの友達を持つユーザーを取得
SELECT user_id AS id, num_friends AS num
FROM FriendCount
-- 友達数の多い順に並べ替える
ORDER BY num_friends DESC
-- 最も多くの友達を持つユーザー1人を取得する
LIMIT 1;
