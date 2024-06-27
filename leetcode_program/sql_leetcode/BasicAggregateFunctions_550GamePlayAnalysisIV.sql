-- プレイヤーごとの最初のログイン日を取得するためのCTE（共通テーブル式）
WITH FirstLogin AS (
    -- 各プレイヤーの最初のログイン日を選択
    SELECT player_id, MIN(event_date) AS first_login_date
    FROM Activity
    GROUP BY player_id
),
-- 最初のログイン日の翌日にログインしたプレイヤーを特定するためのCTE
NextDayLogin AS (
    -- ActivityテーブルとFirstLogin CTEを結合して、最初のログイン日の翌日にログインしたプレイヤーを選択
    SELECT DISTINCT A.player_id
    FROM Activity A
    JOIN FirstLogin F
    ON A.player_id = F.player_id AND A.event_date = DATE_ADD(F.first_login_date, INTERVAL 1 DAY)
)
-- 再ログインしたプレイヤーの割合を計算して結果を出力
SELECT
    -- 再ログインしたプレイヤー数を全プレイヤー数で割って小数点以下2桁に丸めた結果を出力
    ROUND(COUNT(N.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM 
    NextDayLogin N;
