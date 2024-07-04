-- OrderedQueueという共通テーブル式（CTE）を定義します。
-- このCTEでは、turnの順序で並べ替え、累積重量を計算します。
WITH OrderedQueue AS (
    SELECT
        person_id,                           -- 人のID
        person_name,                         -- 人の名前
        weight,                              -- 人の重量
        turn,                                -- バスに乗る順番
        SUM(weight) OVER (ORDER BY turn) AS cumulative_weight  -- 累積重量を計算
    FROM
        Queue                                -- Queueテーブルからデータを取得
),

-- FilteredQueueというCTEを定義します。
-- このCTEでは、累積重量が1000キログラム以下の行のみを選択します。
FilteredQueue AS (
    SELECT
        person_id,                           -- 人のID
        person_name,                         -- 人の名前
        weight,                              -- 人の重量
        turn,                                -- バスに乗る順番
        cumulative_weight                    -- 累積重量
    FROM
        OrderedQueue                         -- OrderedQueue CTEからデータを取得
    WHERE
        cumulative_weight <= 1000            -- 累積重量が1000キログラム以下の行をフィルタリング
)

-- 最後に、FilteredQueue CTEから累積重量が最も大きい行を取得し、そのperson_nameを返します。
SELECT
    person_name                             -- 最後にバスに乗れる人の名前
FROM
    FilteredQueue                           -- FilteredQueue CTEからデータを取得
ORDER BY
    cumulative_weight DESC                  -- 累積重量が大きい順に並べ替え
LIMIT 1;                                    -- 最も累積重量が大きい行を1つだけ取得
