-- 定義されたログデータに対してCTEを使用してデータを準備します
WITH Logs AS (
    -- 各行に対して、前の1行および2行前のidとnumを取得します
    SELECT 
        id, -- 現在の行のid
        num, -- 現在の行のnum
        LAG(id, 1) OVER (ORDER BY id) AS prev_id, -- 1行前のid
        LAG(id, 2) OVER (ORDER BY id) AS prev2_id, -- 2行前のid
        LAG(num, 1) OVER (ORDER BY id) AS prev_num, -- 1行前のnum
        LAG(num, 2) OVER (ORDER BY id) AS prev2_num -- 2行前のnum
    FROM
        Logs -- 元のテーブル
)
-- CTEを使用してメインクエリを実行します
SELECT
    DISTINCT num AS ConsecutiveNums -- 重複を避けるためにDISTINCTを使用して連続するnumを抽出します
FROM
    Logs -- 先に定義したCTEを参照します
WHERE
    num = prev_num AND -- 現在のnumが1行前のnumと等しいことを確認します
    num = prev2_num AND -- 現在のnumが2行前のnumと等しいことを確認します
    id = prev_id + 1 AND -- 現在のidが1行前のidより1大きいことを確認します
    prev_id = prev2_id + 1; -- 1行前のidが2行前のidより1大きいことを確認します
