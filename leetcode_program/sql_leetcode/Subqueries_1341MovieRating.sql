-- -- 最も多くの映画を評価したユーザーの名前を取得
-- SELECT name AS results
-- FROM Users
-- WHERE user_id = (
--     SELECT user_ratings.user_id
--     FROM (
--         SELECT user_id, COUNT(*) AS rating_count
--         FROM MovieRating
--         GROUP BY user_id
--     ) AS user_ratings
--     JOIN Users ON user_ratings.user_id = Users.user_id
--     ORDER BY rating_count DESC, Users.name ASC
--     LIMIT 1
-- )

-- UNION ALL

-- SELECT title AS results
-- FROM Movies
-- WHERE movie_id = (
--     SELECT movie_id
--     FROM (
--         SELECT movie_id, AVG(rating) AS avg_rating
--         FROM MovieRating
--         WHERE created_at BETWEEN '2020-02-01' AND '2020-02-29'
--         GROUP BY movie_id
--     ) AS movie_ratings
--     ORDER BY avg_rating DESC, Movies.title ASC
--     LIMIT 1
-- )


-- 最も多くの映画を評価したユーザーを見つける
WITH UserRankings AS (
    SELECT 
        u.name,                                          -- ユーザー名を選択
        COUNT(*) as movie_count,                         -- 各ユーザーが評価した映画の数をカウント
        ROW_NUMBER() OVER (
            ORDER BY COUNT(*) DESC, u.name ASC           -- 評価数で降順、同数の場合は名前で昇順にランク付け
        ) as user_rank
    FROM MovieRating mr
    JOIN Users u ON mr.user_id = u.user_id               -- MovieRatingテーブルとUsersテーブルを結合
    GROUP BY u.user_id, u.name                           -- ユーザーIDと名前でグループ化
),
-- 2020年2月に最も高い平均評価を得た映画を見つける
MovieRankings AS (
    SELECT 
        m.title,                                         -- 映画のタイトルを選択
        AVG(mr.rating) as avg_rating,                    -- 各映画の平均評価を計算
        ROW_NUMBER() OVER (
            ORDER BY AVG(mr.rating) DESC, m.title ASC    -- 平均評価で降順、同点の場合はタイトルで昇順にランク付け
        ) as movie_rank
    FROM MovieRating mr
    JOIN Movies m ON mr.movie_id = m.movie_id            -- MovieRatingテーブルとMoviesテーブルを結合
    WHERE mr.created_at >= '2020-02-01'                  -- 2020年2月1日以降の評価を選択
      AND mr.created_at < '2020-03-01'                   -- 2020年3月1日未満の評価を選択（2月のみ）
    GROUP BY m.movie_id, m.title                         -- 映画IDとタイトルでグループ化
)
-- 結果を組み合わせる
SELECT name as results                                   -- 最も多くの映画を評価したユーザーの名前を選択
FROM UserRankings
WHERE user_rank = 1                                      -- ランクが1位（最多評価）のユーザーのみ選択
UNION ALL                                                -- 以下のクエリ結果と結合（重複を許可）
SELECT title                                             -- 最高平均評価の映画のタイトルを選択
FROM MovieRankings
WHERE movie_rank = 1;                                    -- ランクが1位（最高平均評価）の映画のみ選択