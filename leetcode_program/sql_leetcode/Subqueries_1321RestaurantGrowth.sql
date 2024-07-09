-- 顧客の訪問日ごとの合計支払額を計算するサブクエリ
WITH DailyTotals AS (
    SELECT
        visited_on,                  -- 訪問日
        SUM(amount) AS daily_total   -- 訪問日ごとの合計支払額
    FROM
        Customer                     -- 顧客テーブルから
    GROUP BY
        visited_on                   -- 訪問日ごとにグループ化
),

-- 訪問日ごとの過去7日間の合計支払額と平均支払額を計算するサブクエリ
MovingAverages AS (
    SELECT
        dt1.visited_on,              -- 基準となる訪問日
        SUM(dt2.daily_total) AS amount,           -- 過去7日間の合計支払額
        ROUND(AVG(dt2.daily_total), 2) AS average_amount  -- 過去7日間の平均支払額（小数点以下2桁に丸める）
    FROM
        DailyTotals dt1              -- 基準日を含むテーブル
    JOIN
        DailyTotals dt2              -- 過去7日間を含むテーブル
    ON
        dt2.visited_on BETWEEN DATE_SUB(dt1.visited_on, INTERVAL 6 DAY) AND dt1.visited_on  -- 基準日を含む過去7日間の範囲指定
    GROUP BY
        dt1.visited_on               -- 基準日ごとにグループ化
)

-- 最終結果の選択と表示
SELECT
    visited_on,                      -- 訪問日
    amount,                          -- 過去7日間の合計支払額
    average_amount                   -- 過去7日間の平均支払額
FROM
    MovingAverages                   -- 上記で計算された移動平均のサブクエリから
WHERE
    visited_on >= (SELECT MIN(visited_on) + INTERVAL 6 DAY FROM Customer)  -- 移動平均計算開始日以降のデータをフィルタリング
ORDER BY
    visited_on;                      -- 訪問日で昇順に並べ替え
